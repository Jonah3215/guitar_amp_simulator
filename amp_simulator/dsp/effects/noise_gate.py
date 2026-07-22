import numpy as np
from ..core.filters import OnePoleFilter

class NoiseGate:
    def __init__(self):
        # envelope follower
        self.env_filter = OnePoleFilter()

        # current gain applied to signal
        self.gain = 1.0

        # Assuming standard sample rate. Change this if your system uses 48000!
        self.sample_rate = 44100.0 

    def process(self, x, params):
        # 1. Map GUI knobs ONCE outside the loop
        threshold = self.map_knob(params.noise_gate_threshold, 0.001, 0.20)
        threshold_close = threshold * 0.8  # Hysteresis safe zone
        
        # Envelope smoothness (keep this very high so the envelope doesn't jitter)
        env_coeff = 0.999 

        # 2. Map Attack/Decay to TIME (in seconds)
        # Attack: 1ms (fastest) to 50ms (slowest)
        attack_time = self.map_knob(10 - params.noise_gate_attack, 0.001, 0.050)
        
        # Decay: 10ms (fastest) to 500ms (slowest)
        decay_time = self.map_knob(params.noise_gate_decay, 0.010, 0.500)

        # 3. Calculate step size per sample
        # Formula: 1.0 (full volume) / (Total Samples it takes to finish the fade)
        attack_step = 1.0 / (self.sample_rate * attack_time)
        decay_step = 1.0 / (self.sample_rate * decay_time)

        y = np.zeros_like(x)

        # process each sample
        for i, sample in enumerate(x):
            
            # estimate envelope
            current_env = self.env_filter.process_sample(abs(sample), env_coeff)

            # decide target state using Hysteresis
            if self.gain > 0.5:
                # Gate is mostly open, use lower threshold
                target_gain = 1.0 if current_env > threshold_close else 0.0
            else:
                # Gate is mostly closed, use upper threshold
                target_gain = 1.0 if current_env > threshold else 0.0

            # LINEAR RAMPING: The Nuclear Option
            if self.gain < target_gain:
                # Fading IN: Add step, but don't overshoot target_gain
                self.gain = min(self.gain + attack_step, target_gain)
            elif self.gain > target_gain:
                # Fading OUT: Subtract step, but don't undershoot target_gain
                self.gain = max(self.gain - decay_step, target_gain)

            # apply gate gain
            y[i] = sample * self.gain

        return y

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        self.env_filter.reset()
        self.gain = 1.0