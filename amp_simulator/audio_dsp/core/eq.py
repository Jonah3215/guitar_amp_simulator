from ..core.filters import OnePoleFilter

class ThreeBandEQ:
    def __init__(self):
        self.low_lp = OnePoleFilter()
        self.mid_lp = OnePoleFilter()

    def process(self, x, params):
        low = self.low_lp.process(x, a=0.99)     # low frequencies        
        low_mid = self.mid_lp.process(x, a=0.80) # low and mid frequencies

        bass_band = low
        mid_band = low_mid - low      # (Bass + Mids) - Bass = Mids
        treble_band = x - low_mid     # Original - (Bass + Mids) = Treble

        bass_band *= params.bass / 10.0
        mid_band *= params.mids / 10.0
        treble_band *= params.treble / 10.0

        return bass_band + mid_band + treble_band