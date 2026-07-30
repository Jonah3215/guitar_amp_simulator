import numpy as np
from ..core.filters import OnePoleFilter

class Overdrive:
    def __init__(self):
        self.tone_filter = OnePoleFilter()

    def process(self, x, params):
        # map knobs
        drive = self.map_knob(params.overdrive_drive, 1.0, 10.0)
        tone_coeff = self.map_knob(10.0 - params.overdrive_tone, 0.10, 0.95)
        level = self.map_knob(params.overdrive_level, 0.5, 2.0)

        x = x * drive                                 # input gain (drive knob)
        x = np.tanh(x)                                # tanh soft clipping
        x = self.tone_filter.process(x, tone_coeff)   # tone filter (tone knob)
        x = x * level                                 # output gain (level knob)

        return x

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        self.tone_filter.reset()