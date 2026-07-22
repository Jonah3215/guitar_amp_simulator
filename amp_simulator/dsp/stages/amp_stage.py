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
    # 1. Guaranteed clean pass-through at drive = 0.
    # We map the drive (assuming a 0 to 10 knob) to a wet/dry mix.
    mix = np.clip(drive / 10.0, 0.0, 1.0)
    
    if mix == 0.0:
        return x
        
    # 2. Gentle gain for "Edge of Breakup" warmth.
    # Instead of muting at 0, the base gain is 1.0 (unity). 
    # Turning the drive up to 10 maxes out at a subtle 4.0 multiplier.
    gain = 1.0 + (drive * 0.3)
    x_driven = x * gain
    
    # 3. Asymmetric Tube Soft-Clipping without the "Fizz"
    # Dividing the negative side by 0.8 forces the slope to exactly match 
    # the positive side's slope at the zero-crossing, preventing harsh harmonics.
    pos = np.tanh(x_driven)
    neg = np.tanh(0.8 * x_driven) / 0.8
    
    saturated = np.where(x_driven >= 0, pos, neg)
    
    # 4. Volume Compensation and Blending
    # tanh naturally lowers the peak volume as it squashes the wave. 
    # We add a little makeup gain so the amp feels powerful as it saturates.
    makeup_gain = np.sqrt(gain)
    
    return (1.0 - mix) * x + (mix * saturated * makeup_gain)

def amp_volume(x, volume):
    return x * (volume / 10.0)