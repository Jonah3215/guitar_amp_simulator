import numpy as np

class Analysis:
    def __init__(self):
        # time domain information
        self.dry_waveform = np.array([], dtype=float)
        self.wet_waveform = np.array([], dtype=float)

        # frequency domain information
        self.frequencies  = np.array([], dtype=float)
        self.dry_spectrum = np.array([], dtype=float)
        self.wet_spectrum = np.array([], dtype=float)
    

    def update_frequency_axis(self, sample_rate, block_size):
        self.frequencies = np.fft.rfftfreq(
            block_size,
            1 / sample_rate
        )
        
        # clear old data
        self.dry_waveform = np.array([], dtype=float)
        self.wet_waveform = np.array([], dtype=float)
        self.dry_spectrum = np.array([], dtype=float)
        self.wet_spectrum = np.array([], dtype=float)