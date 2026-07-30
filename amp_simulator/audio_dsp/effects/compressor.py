import numpy as np
from ..core.filters import OnePoleFilter

class Compressor:
    def __init__(self):
        self.env_filter = OnePoleFilter()
        self.gain = 1.0
        self.env_coeff = 0.95 

    def process(self, x, params):
        threshold = self.map_knob(params.compressor_threshold, 0.01, 1.0)
        ratio = self.map_knob(params.compressor_ratio, 1.0, 20.0)
        a_attack = self.map_knob(10.0 - params.compressor_attack, 0.90, 0.999)
        a_decay = self.map_knob(params.compressor_decay, 0.99, 0.999)
        makeup = self.map_knob(params.compressor_makeup, 1.0, 4.0) # makeup gain to +[0-12 dB]

        y = np.zeros_like(x)

        # process each sample 
        for i, sample in enumerate(x):
            
            # estimate envelope
            envelope = self.env_filter.process_sample(abs(sample), self.env_coeff)

            # compute desired gain
            target_gain = self.compute_gain(envelope, threshold, ratio)

            # decide whether to use gain or decay
            a = a_attack if target_gain < self.gain else a_decay
            self.gain = (1 - a) * target_gain + a * self.gain

            # apply to output
            y[i] = sample * self.gain * makeup

        return y

    def compute_gain(self, envelope, threshold, ratio):
        # if signal is below threshold (or ~zero), no gain reduction
        if envelope <= threshold or envelope < 1e-6:
            return 1.0
            
        # convert to dB scale for ratio math
        envelope_db = 20.0 * np.log10(envelope)
        threshold_db = 20.0 * np.log10(threshold)
        
        # calculate the overshoot and the required reduction
        overshoot_db = envelope_db - threshold_db
        gain_reduction_db = overshoot_db * (1.0 - (1.0 / ratio))
    
        # convert reduction back to linear multiplier (< 1.0)
        target_gain = 10.0 ** (-gain_reduction_db / 20.0)
        
        # clamp to ensure floating-point anomalies doesn't cause gain > 1.0
        return np.clip(target_gain, 0.0, 1.0)

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        self.env_filter.reset()
        self.gain = 1.0