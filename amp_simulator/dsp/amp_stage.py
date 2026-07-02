# The main amp stage of the signal chain

import numpy as np
from .eq import ThreeBandEQ

eq = ThreeBandEQ()

def amp_stage(x, params):
    x = amp_gain(x, params.gain)
    x = amp_drive(x, params.drive)
    x = amp_eq(x, params.bass, params.mid, params.treble)
    x = amp_volume(x, params.volume)

    return x

def amp_gain(x, gain):
    return x * gain

def amp_drive(x, drive):
    return np.tanh(x * drive)

def amp_eq(x, bass, mid, treble):
    return eq.process(
        x,
        bass=bass,
        mid=mid,
        treble=treble
    )

def amp_volume(x, volume):
    return x * (volume / 10.0)