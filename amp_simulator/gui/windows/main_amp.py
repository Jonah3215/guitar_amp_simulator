import dearpygui.dearpygui as dpg

def create_tab(app):
    cabinet = app.cabinet
    params = app.params

    def update_gain(sender, app_data):
        params.gain = app_data

    def update_drive(sender, app_data):
        params.drive = app_data

    def update_bass(sender, app_data):
        params.bass = app_data

    def update_mid(sender, app_data):
        params.mids = app_data

    def update_treble(sender, app_data):
        params.treble = app_data

    def update_volume(sender, app_data):
        params.volume = app_data

    def update_ir(sender, app_data):
        cabinet.load_ir(app.ir_list[app.ir_list.index(app_data)])
        
    def toggle_ir(sender, app_data):
        params.ir_enabled = app_data

    dpg.add_knob_float(
        label="Gain",
        default_value=params.gain,
        min_value=0.0,
        max_value=10.0,
        callback=update_gain
    )

    dpg.add_spacing(count=2)

    dpg.add_knob_float(
        label="Drive",
        default_value=params.drive,
        min_value=0.0,
        max_value=10.0,
        callback=update_drive
    )

    dpg.add_spacing(count=2)

    dpg.add_knob_float(
        label="Volume",
        default_value=params.volume,
        min_value=0.0,
        max_value=10.0,
        callback=update_volume
    )

    dpg.add_spacing(count=2)

    dpg.add_knob_float(
        label="Bass",
        default_value=params.bass,
        min_value=0.0,
        max_value=10.0,
        callback=update_bass
    )

    dpg.add_spacing(count=2)

    dpg.add_knob_float(
        label="Mids",
        default_value=params.mids,
        min_value=0.0,
        max_value=10.0,
        callback=update_mid
    )

    dpg.add_spacing(count=2)

    dpg.add_knob_float(
        label="Treble",
        default_value=params.treble,
        min_value=0.0,
        max_value=10.0,
        callback=update_treble
    )

    dpg.add_spacing(count=2)

    dpg.add_combo(
        label="Impulse Response",
        items = app.ir_list,
        default_value=app.ir_list[0],
        callback=update_ir
    )

    dpg.add_checkbox(
        label="Enable IR",
        default_value=params.ir_enabled,
        callback=toggle_ir
)