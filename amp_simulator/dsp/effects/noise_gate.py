import numpy as np
from ..core.filters import OnePoleFilter

class NoiseGate:
    def __init__(self):
        # envelope follower
        self.env_filter = OnePoleFilter()

        # current gain applied to signal
        self.gain = 1.0

    def process(self, x, params):
        # map GUI knobs [0, 10] into DSP values
        threshold = self.map_knob(
            params.noise_gate_threshold,
            0.001,
            0.20
        )

        # lower coefficient => faster response
        # invert the knob so higher value means faster attack
        a_attack = self.map_knob(
            10 - params.noise_gate_attack,
            0.0,
            0.999
        )

        # higher coefficient => slower closing
        a_decay = self.map_knob(
            params.noise_gate_decay,
            0.0,
            0.999
        )

        # controls how quickly envelope follows input loudness
        # might parametrize and make into a knob
        env_coeff = 0.8

        y = np.zeros_like(x)

        # process each sample
        for i, sample in enumerate(x):

            # estimate envelope
            current_env = self.env_filter.process_sample(
                abs(sample),
                env_coeff
            )

            # decide whether gate should be open or closed
            target_gain = 1.0 if current_env > threshold else 0.0

            # smooth gain changes to prevent clicks
            if (target_gain > self.gain):
                a = a_attack
            else:
                a = a_decay

            self.gain = (1 - a) * target_gain + a * self.gain

            # 4. Apply gate gain
            y[i] = sample * self.gain

        return y

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        self.env_filter.reset()
        self.gain = 1.0