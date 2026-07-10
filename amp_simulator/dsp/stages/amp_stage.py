import numpy as np

def amp_stage(x, app):
    params = app.params
    cabinet = app.cabinet
    eq = app.eq
    
    x = amp_gain(x, params.gain)
    x = amp_drive(x, params.drive)
    x = amp_eq(x,
               eq, 
               params.bass, 
               params.mid, 
               params.treble)
    
    if params.ir_enabled:
        x = amp_cabinet(x, cabinet)
        
    x = amp_volume(x, params.volume)

    return x

def amp_gain(x, gain):
    return x * gain

def amp_drive(x, drive):
    # pre-saturation compression
    x = x / (1.0 + np.abs(x))
    
    # drive scaling
    x = x * drive
    
    # bias = 0.2
    pos = np.tanh(1.2 * x)
    neg = np.tanh(0.8 * x)
    
    return np.where(x >= 0, pos, neg)

def amp_eq(x, eq, bass, mid, treble):
    return eq.process(
        x=x,
        bass=bass,
        mid=mid,
        treble=treble
    )

def amp_cabinet(x, cabinet):
    return cabinet.process(x)

def amp_volume(x, volume):
    return x * (volume / 10.0)