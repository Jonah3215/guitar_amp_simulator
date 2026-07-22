import numpy as np

from amp_simulator.dsp.stages.input_stage import input_stage
from amp_simulator.dsp.stages.amp_stage import amp_stage
from amp_simulator.dsp.stages.output_stage import output_stage

# x is the audio information
# params is the parameters instance
def process(x, app): 
    # force audio data to be 32 bit float
    x = x.astype(np.float32)

    x = input_stage(x, app)
    x = amp_stage(x, app)
    # output_stage(x, params)
    
    return x