import numpy as np
import soundfile as sf
import math

class CabinetIR:
    def __init__(self, ir_path=None, block_size=256):
        self.ir = None
        self.ir_fft = None
        self.block_size = block_size
        self.fft_size = None
        self.fft_buffer = None

        if ir_path:
            self.load_ir(ir_path)

    def load_ir(self, path):
        data, sr = sf.read(path)

        # force mono
        if data.ndim > 1:
            data = data.mean(axis=1)

        # convert to float and normalize
        data = data.astype(np.float32)
        data /= np.max(np.abs(data)) + 1e-12

        self.ir = data

        # Size = M + N - 1
        min_fft_size = self.block_size + len(self.ir) - 1
        
        # round up to the next power of 2
        self.fft_size = 1 << math.ceil(math.log2(min_fft_size))

        # pad IR to the new optimized FFT size
        ir_padded = np.zeros(self.fft_size, dtype=np.float32)
        ir_padded[:len(self.ir)] = self.ir

        # precompute the frequency domain IR
        self.ir_fft = np.fft.rfft(ir_padded)

        # reset input buffer to the correct power-of-two size
        self.fft_buffer = np.zeros(self.fft_size, dtype=np.float32)

    def reset(self):
        if self.fft_buffer is not None:
            self.fft_buffer.fill(0)

    def process(self, x):
        if self.ir_fft is None:
            return x

        # force x to be the size of self.block_size
        x = x[:self.block_size]

        # shift the buffer left by one block size
        self.fft_buffer[:-self.block_size] = self.fft_buffer[self.block_size:]
        # insert the new audio at the end
        self.fft_buffer[-self.block_size:] = x

        # X = forward FFT of x
        X = np.fft.rfft(self.fft_buffer)

        # convolution via complex multiplication
        Y = X * self.ir_fft

        # inverse FFT
        y = np.fft.irfft(Y)

        # return 
        return y[-self.block_size:].astype(np.float32)