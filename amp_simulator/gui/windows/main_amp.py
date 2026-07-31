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

        # Input Stage
    dpg.add_text("Input Stage")

    with dpg.group(horizontal=True):
        dpg.add_knob_float(
            label="Gain",
            default_value=app.params.gain,
            min_value=0.0,
            max_value=10.0,
            callback=create_param_callback("gain")
        )

        dpg.add_spacer(width=25)

        dpg.add_knob_float(
            label="Drive",
            default_value=app.params.drive,
            min_value=0.0,
            max_value=10.0,
            callback=create_param_callback("drive")
        )

        dpg.add_spacer(width=25)

        dpg.add_knob_float(
            label="Volume",
            default_value=app.params.volume,
            min_value=0.0,
            max_value=10.0,
            callback=create_param_callback("volume")
        )


    dpg.add_separator()


    # EQ
    dpg.add_text("EQ")

    with dpg.group(horizontal=True):
        dpg.add_knob_float(
            label="Bass",
            default_value=params.bass,
            min_value=0.0,
            max_value=10.0,
            callback=create_param_callback("bass")
        )

        dpg.add_spacer(width=25)

        dpg.add_knob_float(
            label="Mids",
            default_value=params.mids,
            min_value=0.0,
            max_value=10.0,
            callback=create_param_callback("mids")
        )

        dpg.add_spacer(width=25)

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