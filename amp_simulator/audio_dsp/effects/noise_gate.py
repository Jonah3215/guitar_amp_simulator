import numpy as np
from ..core.filters import OnePoleFilter

class NoiseGate:
    def __init__(self, sample_rate):
        self.env_filter = OnePoleFilter() # envelope follower
        self.gain = 1.0
        self.sample_rate = sample_rate

    def process(self, x, params):
        threshold = self.map_knob(params.noise_gate_threshold, 0.001, 0.20)
        threshold_close = threshold * 0.8  # hysteresis safe zone
        env_coeff = 0.999

        attack_time = self.map_knob(10 - params.noise_gate_attack, 0.001, 0.050) # [1, 50] ms
        decay_time = self.map_knob(params.noise_gate_decay, 0.010, 0.500) # [10, 500] ms 

        attack_step = 1.0 / (self.sample_rate * attack_time)
        decay_step = 1.0 / (self.sample_rate * decay_time)

        y = np.zeros_like(x)

        for i, sample in enumerate(x):
            current_env = self.env_filter.process_sample(abs(sample), env_coeff)

            # decide target state using hysteresis
            if (self.gain > 0.5):
                target_gain = 1.0 if (current_env > threshold_close) else 0.0
            else:
                target_gain = 1.0 if (current_env > threshold) else 0.0

            # linear ramping of gain (prevents zippering)
            if (self.gain < target_gain):
                self.gain = min(self.gain + attack_step, target_gain) # fade in
            elif (self.gain > target_gain):
                self.gain = max(self.gain - decay_step, target_gain)  # fade out

            y[i] = sample * self.gain

        return y

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        self.env_filter.reset()
        self.gain = 1.0