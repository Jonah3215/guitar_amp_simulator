import numpy as np
from ..core.filters import OnePoleFilter

class Limiter:
    def __init__(self):
        self.env_filter = OnePoleFilter()
        self.env_coeff = 0.95 

        self.gain = 1.0

        self.attack_coeff = 0.01

    def process(self, x, params):
        # Ceiling: Knob 0 -> -6 dB, Knob 10 -> 0 dB
        ceiling_db = self.map_knob(params.limiter_ceiling, -6.0, 0.0)
        ceiling = 10.0 ** (ceiling_db / 20.0)

        release_coeff = self.map_knob(params.limiter_release, 0.99, 0.9999)

        y = np.zeros_like(x)

        for i, sample in enumerate(x):

            envelope = self.env_filter.process_sample(abs(sample), self.env_coeff)
            target_gain = self.compute_gain(envelope, ceiling)
    
            # if target_gain is lower than current gain, a peak hit and we must reduce volume
            if target_gain < self.gain:
                coeff = self.attack_coeff
            else:
                # otherwise, the peak has passed and we can gradually restore volume
                coeff = release_coeff

            self.gain = (1.0 - coeff) * target_gain + coeff * self.gain

            y[i] = sample * self.gain

        return y

    def compute_gain(self, envelope, ceiling):
        if envelope <= ceiling or envelope < 1e-6:
            return 1.0
            
        # calculate the exact ratio needed to get back to cieling
        return np.clip(ceiling / envelope, 0.0, 1.0)

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        self.env_filter.reset()
        self.gain = 1.0