import numpy as np

def amp_stage(x, app):
    params = app.params
    
    x = amp_gain(x, params.gain)
    x = amp_drive(x, params.drive)
    x = app.eq.process(x, params)
    
    if params.ir_enabled:
        x = app.cabinet.process(x)
        
    x = amp_volume(x, params.volume)

    return x

def amp_gain(x, gain):
    return x * gain

def amp_drive(x, drive):
    mix = np.clip(drive / 10.0, 0.0, 1.0)
    
    if mix == 0.0:
        return x
    
    # gain maxes at  4.0
    drive_gain = 1.0 + (drive * 0.3)
    x_driven = x * drive_gain
    
    # asymmetric tube soft-clipping
    pos = np.tanh(x_driven)
    neg = np.tanh(0.8 * x_driven) / 0.8
    
    saturated = np.where(x_driven >= 0, pos, neg)
    makeup_gain = np.sqrt(drive_gain)
    
    return (1.0 - mix) * x + (mix * saturated * makeup_gain)

def amp_volume(x, volume):
    return x * (volume / 10.0)