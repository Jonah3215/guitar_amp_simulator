import numpy as np

# x is the audio information
# p is the parameters instance
def process(x, p): 
    # force floats
    x = x.astype(np.float32)

    # apply input gain (pre-amp stage)
    x = x * p.gain

    # soft clipping distortion (amp saturation)
    x = np.tanh(p.drive * x)

    # output volume control 
    x = x * (p.volume / 10.0)

    return x