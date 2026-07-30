import dearpygui.dearpygui as dpg

def create_tab(app):
    cabinet = app.cabinet
    params = app.params

    def create_param_callback(parameter):
        def callback(sender, app_data):
            setattr(params, parameter, app_data)
        return callback

    def update_ir(sender, app_data):
        cabinet.load_ir(app.ir_list[app.ir_list.index(app_data)])

    # Main Amp UI
    dpg.add_text("Main Amp Controls")

    dpg.add_separator()

    # Gain knob
    dpg.add_knob_float(
        label="Gain",
        default_value=params.gain,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("gain")
    )

    # Drive knob
    dpg.add_knob_float(
        label="Drive",
        default_value=params.drive,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("drive")
    )

    # Volume knob
    dpg.add_knob_float(
        label="Volume",
        default_value=params.volume,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("volume")
    )

    # Bass knob
    dpg.add_knob_float(
        label="Bass",
        default_value=params.bass,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("bass")
    )

    # Mids knob
    dpg.add_knob_float(
        label="Mids",
        default_value=params.mids,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("mids")
    )

    # Treble knob
    dpg.add_knob_float(
        label="Treble",
        default_value=params.treble,
        min_value=0.0,
        max_value=10.0,
        callback=create_param_callback("treble")
    )

    # IR dropdown menu
    dpg.add_combo(
        label="Impulse Response",
        items=app.ir_list,
        default_value=app.ir_list[0],
        callback=update_ir
    )

    # IR Checkbox
    dpg.add_checkbox(
        label="Enable IR",
        default_value=params.ir_enabled,
        callback=create_param_callback("ir_enabled")
    )