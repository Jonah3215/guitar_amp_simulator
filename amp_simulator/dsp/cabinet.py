import numpy as np
from scipy.io import wavfile

class CabinetIR:
    def __init__(self, ir_path=None, fft_size=2048, block_size=256):
        self.ir = None
        self.ir_fft = None

        # block size (size of incoming audio chunks)
        self.block_size = block_size

        # convolution size (computed after IR is loaded)
        self.n_fft = None

        # leftover audio from previous block convolution (initialize to 0s)
        self.overlap = None

        if ir_path:
            self.load_ir(ir_path)

    def load_ir(self, path):
        # load IR from wav file
        sr, data = wavfile.read(path)

        # force IR to mono)
        if data.ndim > 1:
            data = data.mean(axis=1)

        # convert to float and normalize, +1e-12 prevents divide-by-zero
        data = data.astype(np.float32)
        data /= np.max(np.abs(data)) + 1e-12

        self.ir = data

        # compute the FFT size (N + M - 1)
        self.n_fft = self.block_size + len(self.ir) - 1

        # precompute FFT of IR
        self.ir_fft = np.fft.rfft(self.ir, n=self.n_fft)

        # reset overlap buffer for new IR
        self.overlap = np.zeros(self.n_fft, dtype=np.float32)

    def reset(self):
        # clears leftover convolution tail
        # call when switching IRs or restarting audio stream
        if self.overlap is not None:
            self.overlap.fill(0)

    def process(self, x):
        # if no IR loaded, just return the original signal
        if self.ir_fft is None:
            return x

        n = self.n_fft

        # zero-pad the input buffer to the FFT size
        x_pad = np.zeros(n, dtype=np.float32)
        x_pad[:len(x)] = x

        # apply convolution theorem
        X = np.fft.rfft(x_pad)
        Y = X * self.ir_fft
        y = np.fft.irfft(Y)

        # overlap stores leftover from previous block
        output = y[:len(x)] + self.overlap[:len(x)]

        # store new tail for next block
        self.overlap = y[len(x):]

        return output.astype(np.float32)