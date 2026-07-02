import numpy as np
from .filters import OnePoleLowPass, OnePoleHighPass

class ThreeBandEQ:
    def __init__(self):
        self.low = OnePoleLowPass()
        self.high = OnePoleHighPass()

    def process(self, x, bass, mid, treble):
        # normalize knobs from [0, 10] to [0, 1]
        bass /= 10.0
        mid /= 10.0
        treble /= 10.0

        # split signal into frequency regions
        low = self.low.process(x, cutoff=0.05)
        high = self.high.process(x, cutoff=0.05)
        mid_band = x - (low + high)

        # apply gain per band
        low *= bass
        mid_band *= mid
        high *= treble

        # recombine
        return low + mid_band + high