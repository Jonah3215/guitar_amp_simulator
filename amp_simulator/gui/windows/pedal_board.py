import dearpygui.dearpygui as dpg

def create_tab(app):
    params = app.params

    # noise gate callbacks
    def update_noise_gate_enabled(sender, app_data):
        params.noise_gate_enabled = app_data

    def update_noise_gate_threshold(sender, app_data):
        params.noise_gate_threshold = app_data

    def update_noise_gate_attack(sender, app_data):
        params.noise_gate_attack = app_data

    def update_noise_gate_decay(sender, app_data):
        params.noise_gate_decay = app_data

    # compressor callbacks
    def update_compressor_enabled(sender, app_data):
        params.compressor_enabled = app_data

    def update_compressor_threshold(sender, app_data):
        params.compressor_threshold = app_data

    def update_compressor_ratio(sender, app_data):
        params.compressor_ratio = app_data

    def update_compressor_attack(sender, app_data):
        params.compressor_attack = app_data

    def update_compressor_decay(sender, app_data):
        params.compressor_decay = app_data

    def update_compressor_makeup(sender, app_data):
        params.compressor_makeup = app_data

    # pedal board UI 
    dpg.add_text("Pedal Board")

    dpg.add_separator()

    # Noise Gate
    dpg.add_text("Noise Gate")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.noise_gate_enabled,
        callback=update_noise_gate_enabled
    )

    dpg.add_knob_float(
        label="Threshold",
        default_value=params.noise_gate_threshold,
        min_value=0.0,
        max_value=10.0,
        callback=update_noise_gate_threshold
    )

    dpg.add_knob_float(
        label="Attack",
        default_value=params.noise_gate_attack,
        min_value=0.0,
        max_value=10.0,
        callback=update_noise_gate_attack
    )

    dpg.add_knob_float(
        label="Decay",
        default_value=params.noise_gate_decay,
        min_value=0.0,
        max_value=10.0,
        callback=update_noise_gate_decay
    )


    dpg.add_separator()

    # Compressor
    dpg.add_text("Compressor")

    dpg.add_checkbox(
        label="Enabled",
        default_value=params.compressor_enabled,
        callback=update_compressor_enabled
    )

    dpg.add_knob_float(
        label="Threshold",
        default_value=params.compressor_threshold,
        min_value=0.0,
        max_value=10.0,
        callback=update_compressor_threshold
    )

    dpg.add_knob_float(
        label="Ratio",
        default_value=params.compressor_ratio,
        min_value=0.0,
        max_value=10.0,
        callback=update_compressor_ratio
    )

    dpg.add_knob_float(
        label="Attack",
        default_value=params.compressor_attack,
        min_value=0.0,
        max_value=10.0,
        callback=update_compressor_attack
    )

    dpg.add_knob_float(
        label="Decay",
        default_value=params.compressor_decay,
        min_value=0.0,
        max_value=10.0,
        callback=update_compressor_decay
    )

    dpg.add_knob_float(
        label="Makeup",
        default_value=params.compressor_makeup,
        min_value=0.0,
        max_value=10.0,
        callback=update_compressor_makeup
    )

    dpg.add_separator()
    # Future effects
    dpg.add_text("Future Effects")

    dpg.add_checkbox(label="Overdrive")

    dpg.add_checkbox(label="Chorus")

    dpg.add_checkbox(label="Delay")

    dpg.add_checkbox(label="Reverb")