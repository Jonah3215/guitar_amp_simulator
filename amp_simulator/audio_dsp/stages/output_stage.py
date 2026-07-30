def output_stage(x, app):
    params = app.params

    if (params.reverb_enabled):
        x = app.reverb.process(x, params)

    x = x * params.master_volume / 10.0

    if (params.limiter_enabled):
        x = app.limiter.process(x, params)

    return x