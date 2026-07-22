from ..core.filters import OnePoleFilter

class ThreeBandEQ:
    def __init__(self):
        self.low_lp = OnePoleFilter()
        self.mid_lp = OnePoleFilter()
        # We don't even need high_hp! Subtraction handles the treble perfectly.

    def process(self, x, params):
        # 1. High coefficient (e.g., 0.99) = heavy filtering. ONLY Bass gets through.
        low = self.low_lp.process(x, a=0.99)
        
        # 2. Lower coefficient (e.g., 0.80) = wider filtering. Bass + Mids get through.
        low_mid = self.mid_lp.process(  x, a=0.80)

        # 3. Split into bands (Perfect Reconstruction)
        bass_band = low
        mid_band = low_mid - low      # (Bass + Mids) - Bass = Mids
        treble_band = x - low_mid     # Original - (Bass + Mids) = Treble

        # 4. Apply gains 
        bass_band *= params.bass / 10.0
        mid_band *= params.mids / 10.0
        treble_band *= params.treble / 10.0

        return bass_band + mid_band + treble_band