import numpy as np
import soundfile as sf
import math

class CabinetIR:
    def __init__(self, block_size, ir_path=None):
        self.ir = None
        self.ir_fft = None
        self.block_size = block_size
        self.fft_size = None
        self.fft_buffer = None

        if ir_path:
            self.load_ir(ir_path)

    # define load_ir and store to compute FFT just once upon
    def load_ir(self, path):
        data, sr = sf.read(path)

        # force mono
        if data.ndim > 1:
            data = data.mean(axis=1)

        data = data.astype(np.float32)
        data /= np.max(np.abs(data)) + 1e-12

        self.ir = data

        min_fft_size = self.block_size + len(self.ir) - 1   # Size = M + N - 1
        
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
        if (self.fft_buffer is not None):
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

        # Apply convolution theorem 
        X = np.fft.rfft(self.fft_buffer) # FFT(x)
        Y = X * self.ir_fft              # FFT(IR) ⋅ FFT(X)
        y = np.fft.irfft(Y)              # y = IFFT(Y)

        return y[-self.block_size:].astype(np.float32)