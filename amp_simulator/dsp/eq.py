import numpy as np
from .filters import OnePoleLowPass, OnePoleHighPass

class ThreeBandEQ:
    def __init__(self):
        self.low_lp = OnePoleLowPass()
        self.mid_lp = OnePoleLowPass()
        
    def process(self, x, bass, mid, treble):
        bass /= 10.0
        mid /= 10.0
        treble /= 10.0

        # Two crossover frequencies
        low = self.low_lp.process(x, cutoff=0.02)
        low_mid = self.mid_lp.process(x, cutoff=0.20)

        # Split into bands
        bass_band = low
        mid_band = low_mid - low
        treble_band = x - low_mid

        # Apply gains
        bass_band *= bass
        mid_band *= mid
        treble_band *= treble

        return bass_band + mid_band + treble_band