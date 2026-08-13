import dearpygui.dearpygui as dpg
import sounddevice as sd

def create_tab(app):
    config = app.config

    def refresh_devices():
        devices = sd.query_devices()

        input_devices = []
        output_devices = []

        for index, device in enumerate(devices):

            device_name = f"{index}: {device['name']}"

            if device["max_input_channels"] > 0:
                input_devices.append(device_name)

            if device["max_output_channels"] > 0:
                output_devices.append(device_name)

        dpg.configure_item(
            "input_device",
            items=input_devices
        )

        dpg.configure_item(
            "output_device",
            items=output_devices
        )

    def apply_settings():
        config.sample_rate = int(dpg.get_value("sample_rate"))
        config.block_size = int(dpg.get_value("block_size"))

        input_selection = dpg.get_value("input_device")
        output_selection = dpg.get_value("output_device")

        if input_selection:
            config.input_device = int(input_selection.split(":")[0])

        if output_selection:
            config.output_device = int(output_selection.split(":")[0])

        # Restart the audio engine using the new settings
        app.audio_engine.restart()

    dpg.add_text("Audio Settings")

    dpg.add_separator()

    dpg.add_combo(
        tag="sample_rate",
        label="Sample Rate",
        items=[
            "44100",
            "48000",
            "88200",
            "96000",
            "176400",
            "192000"
        ],
        default_value=str(config.sample_rate)
    )

    dpg.add_combo(
        tag="block_size",
        label="Block Size",
        items=[
            "16",
            "32",
            "48",
            "64",
            "96",
            "128",
            "160",
            "192",
            "256",
            "512",
            "1024"
        ],
        default_value=str(config.block_size)
    )

    dpg.add_combo(
        tag="input_device",
        label="Input Device",
        items=[]
    )

    dpg.add_combo(
        tag="output_device",
        label="Output Device",
        items=[]
    )

    dpg.add_button(
        label="Refresh Devices",
        callback=refresh_devices
    )

    dpg.add_button(
        label="Apply Settings",
        callback=apply_settings
    )

    # Populate device lists when the tab is first created
    refresh_devices()