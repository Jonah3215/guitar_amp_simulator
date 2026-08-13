import dearpygui.dearpygui as dpg

def create_tab(app):
    cabinet = app.cabinet
    params = app.params

    def create_param_callback(parameter):
        def callback(sender, app_data):
            setattr(params, parameter, app_data)
        return callback

    def add_knob(label, parameter):
        dpg.add_knob_float(
            label=label,
            default_value=getattr(params, parameter),
            min_value=0.0,
            max_value=10.0,
            callback=create_param_callback(parameter)
        )

    def add_section(title, knobs):
    # Section title
        dpg.add_text(title)

        # Everything in this row
        with dpg.group(horizontal=True):

            # Knobs
            for label, parameter in knobs:
                add_knob(label, parameter)
                dpg.add_spacer(width=30)

        dpg.add_separator()

    def update_ir(sender, app_data):
        cabinet.load_ir(app_data)

    # Main Amp UI
    
    dpg.add_text("Main Amp Controls")
    dpg.add_separator()

    # Input Stage
    add_section(
        "Input Stage",
        [
            ("Gain", "gain"),
            ("Drive", "drive"),
            ("Volume", "volume")
        ]
    )

    # EQ
    add_section(
        "EQ",
        [
            ("Bass", "bass"),
            ("Mids", "mids"),
            ("Treble", "treble")
        ]
    )

    # Cabinet
    dpg.add_text("Cabinet")

    dpg.add_combo(
        label="Impulse Response",
        items=app.ir_list,
        default_value=app.ir_list[0],
        callback=update_ir
    )

    dpg.add_checkbox(
        label="Enable IR",
        default_value=params.ir_enabled,
        callback=create_param_callback("ir_enabled")
    )