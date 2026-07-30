import dearpygui.dearpygui as dpg

def create_tab(app):
    params = app.params

    def create_param_callback(parameter):
        def callback(sender, app_data):
            setattr(params, parameter, app_data)
        return callback

    # Input Effects UI
    dpg.add_text("Input Effect Controls")

    dpg.add_separator()

    # Noise Gate
    dpg.add_text("Noise Gate")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.noise_gate_enabled,
        callback=create_param_callback("noise_gate_enabled")
    )

    dpg.add_knob_float(
        label="Threshold",
        default_value=params.noise_gate_threshold,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("noise_gate_threshold")
    )

    dpg.add_knob_float(
        label="Attack",
        default_value=params.noise_gate_attack,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("noise_gate_attack")
    )

    dpg.add_knob_float(
        label="Decay",
        default_value=params.noise_gate_decay,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("noise_gate_decay")
    )

    dpg.add_separator()

    # Compressor
    dpg.add_text("Compressor")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.compressor_enabled,
        callback=create_param_callback("compressor_enabled")
    )

    dpg.add_knob_float(
        label="Threshold",
        default_value=params.compressor_threshold,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("compressor_threshold")
    )

    dpg.add_knob_float(
        label="Ratio",
        default_value=params.compressor_ratio,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("compressor_ratio")
    )

    dpg.add_knob_float(
        label="Attack",
        default_value=params.compressor_attack,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("compressor_attack")
    )

    dpg.add_knob_float(
        label="Decay",
        default_value=params.compressor_decay,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("compressor_decay")
    )

    dpg.add_knob_float(
        label="Makeup",
        default_value=params.compressor_makeup,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("compressor_makeup")
    )

    dpg.add_separator()

    # Overdrive
    dpg.add_text("Overdrive")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.overdrive_enabled,
        callback=create_param_callback("overdrive_enabled")
    )

    dpg.add_knob_float(
        label="Drive",
        default_value=params.overdrive_drive,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("overdrive_drive")
    )

    dpg.add_knob_float(
        label="Tone",
        default_value=params.overdrive_tone,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("overdrive_tone")
    )

    dpg.add_knob_float(
        label="Level",
        default_value=params.overdrive_level,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("overdrive_level")
    )

    dpg.add_separator()

    # Chorus
    dpg.add_text("Chorus")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.chorus_enabled,
        callback=create_param_callback("chorus_enabled")
    )

    dpg.add_knob_float(
        label="Rate",
        default_value=params.chorus_rate,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("chorus_rate")
    )

    dpg.add_knob_float(
        label="Depth",
        default_value=params.chorus_depth,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("chorus_depth")
    )

    dpg.add_knob_float(
        label="Mix",
        default_value=params.chorus_mix,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("chorus_mix")
    )

    dpg.add_separator()

    # Delay
    dpg.add_text("Delay")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.delay_enabled,
        callback=create_param_callback("delay_enabled")
    )

    dpg.add_knob_float(
        label="Time",
        default_value=params.delay_time,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("delay_time")
    )

    dpg.add_knob_float(
        label="Feedback",
        default_value=params.delay_feedback,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("delay_feedback")
    )

    dpg.add_knob_float(
        label="Mix",
        default_value=params.delay_mix,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("delay_mix")
    )