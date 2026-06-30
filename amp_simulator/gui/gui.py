import dearpygui.dearpygui as dpg

def start_gui(params):
    dpg.create_context()
    dpg.create_viewport(title="Amp Simulator", width=1000, height=500)

    with dpg.window(label="Amp Control Panel", width=980, height=460):

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

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()