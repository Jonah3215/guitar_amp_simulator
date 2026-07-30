import dearpygui.dearpygui as dpg

def create_tab(app):
    params = app.params

    def create_param_callback(parameter):
        def callback(sender, app_data):
            setattr(params, parameter, app_data)
        return callback

    dpg.add_text("Output Effect Controls")

    dpg.add_separator()

    # Reverb
    dpg.add_text("Reverb")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.reverb_enabled,
        callback=create_param_callback("reverb_enabled")
    )

    dpg.add_knob_float(
        label="Decay",
        default_value=params.reverb_decay,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("reverb_decay")
    )

    dpg.add_knob_float(
        label="Damping",
        default_value=params.reverb_damping,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("reverb_damping")
    )

    dpg.add_knob_float(
        label="Mix",
        default_value=params.reverb_mix,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("reverb_mix")
    )

    dpg.add_separator()

    # Master Volume
    dpg.add_text("Master Volume")

    dpg.add_knob_float(
        label="Volume",
        default_value=params.master_volume,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("master_volume")
    )

    dpg.add_separator()

    # Limiter
    dpg.add_text("Limiter")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.limiter_enabled,
        callback=create_param_callback("limiter_enabled")
    )

    dpg.add_knob_float(
        label="Ceiling",
        default_value=params.limiter_ceiling,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("limiter_ceiling")
    )

    dpg.add_knob_float(
        label="Release",
        default_value=params.limiter_release,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("limiter_release")
    )