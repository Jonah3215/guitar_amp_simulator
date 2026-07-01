import dearpygui.dearpygui as dpg


def create_tab(params):

    def update_gain(sender, app_data):
        params.gain = app_data

    def update_drive(sender, app_data):
        params.drive = app_data

    def update_volume(sender, app_data):
        params.volume = app_data

    dpg.add_text("Input Stage")

    dpg.add_knob_float(
        label="Gain",
        default_value=params.gain,
        min_value=0.0,
        max_value=10.0,
        callback=update_gain
    )

    dpg.add_spacing(count=2)

    dpg.add_text("Amp Drive Stage")

    dpg.add_knob_float(
        label="Drive",
        default_value=params.drive,
        min_value=0.0,
        max_value=10.0,
        callback=update_drive
    )

    dpg.add_spacing(count=2)

    dpg.add_text("Output Stage")

    dpg.add_knob_float(
        label="Volume",
        default_value=params.volume,
        min_value=0.0,
        max_value=10.0,
        callback=update_volume
    )