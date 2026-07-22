import numpy as np

def input_stage(x, app):
    params = app.params

    if (params.noise_gate_enabled):
        x = app.noise_gate.process(x, params)

    if (params.compressor_enabled):
        x = app.compressor.process(x, params)

    return x 