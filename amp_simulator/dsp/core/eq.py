from ..core.filters import OnePoleFilter, OnePoleHighPass

class ThreeBandEQ:
    def __init__(self):
        self.low_lp = OnePoleFilter()
        self.mid_lp = OnePoleFilter()
        self.high_hp = OnePoleHighPass()

    def process(self, x, bass, mid, treble):

        # convert knobs [0,10] to gain multipliers
        bass /= 10.0
        mid /= 10.0
        treble /= 10.0

        # two crossover frequencies
        low = self.low_lp.process(x, a=0.02)
        low_mid = self.mid_lp.process(x, a=0.20)

        # split into bands
        bass_band = low
        mid_band = low_mid - low
        treble_band = self.high_hp.process(x, a=0.20)

        # apply gains
        bass_band *= bass
        mid_band *= mid
        treble_band *= treble

        return bass_band + mid_band + treble_band