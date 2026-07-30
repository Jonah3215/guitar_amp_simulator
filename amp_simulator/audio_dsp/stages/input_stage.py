def input_stage(x, app):
    params = app.params

    if (params.noise_gate_enabled):
        x = app.noise_gate.process(x, params)

    if (params.compressor_enabled):
        x = app.compressor.process(x, params)

    if (params.overdrive_enabled):
        x = app.overdrive.process(x, params)

    if (params.chorus_enabled):
        x = app.chorus.process(x, params)

    if (params.delay_enabled):
        x = app.delay.process(x, params)

    return x  