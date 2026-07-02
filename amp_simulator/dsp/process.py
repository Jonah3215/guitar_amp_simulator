import numpy as np

from amp_simulator.dsp.input_stage import input_stage
from amp_simulator.dsp.amp_stage import amp_stage
from amp_simulator.dsp.output_stage import output_stage

# x is the audio information
# params is the parameters instance
def process(x, params): 
    # force audio data to be 32 bit float
    x = x.astype(np.float32)

    # input_stage(x, params)
    x = amp_stage(x, params)
    # output_stage(x, params)
    
    return x