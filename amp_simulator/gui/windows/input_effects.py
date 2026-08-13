import dearpygui.dearpygui as dpg

def create_tab(app):
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

    def add_effect(title, enabled_param, knobs):
        # Effect title
        dpg.add_text(title)

        # Everything in this row
        with dpg.group(horizontal=True):

            # Enable checkbox
            dpg.add_checkbox(
                label="Enabled",
                default_value=getattr(params, enabled_param),
                callback=create_param_callback(enabled_param)
            )

            dpg.add_spacer(width=30)

            # Knobs
            for label, parameter in knobs:
                add_knob(label, parameter)
                dpg.add_spacer(width=30)

        dpg.add_separator()


    # Input Effects UI
    dpg.add_text("Input Effect Controls")
    dpg.add_separator()

    # Noise Gate
    add_effect(
        "Noise Gate",
        "noise_gate_enabled",
        [
            ("Threshold", "noise_gate_threshold"),
            ("Attack", "noise_gate_attack"),
            ("Decay", "noise_gate_decay")
        ]
    )

    # Compressor
    add_effect(
        "Compressor",
        "compressor_enabled",
        [
            ("Threshold", "compressor_threshold"),
            ("Ratio", "compressor_ratio"),
            ("Attack", "compressor_attack"),
            ("Decay", "compressor_decay"),
            ("Makeup", "compressor_makeup")
        ]
    )

    # Overdrive
    add_effect(
        "Overdrive",
        "overdrive_enabled",
        [
            ("Drive", "overdrive_drive"),
            ("Tone", "overdrive_tone"),
            ("Level", "overdrive_level")
        ]
    )

    # Chorus
    add_effect(
        "Chorus",
        "chorus_enabled",
        [
            ("Rate", "chorus_rate"),
            ("Depth", "chorus_depth"),
            ("Mix", "chorus_mix")
        ]
    )

    # Delay
    add_effect(
        "Delay",
        "delay_enabled",
        [
            ("Time", "delay_time"),
            ("Feedback", "delay_feedback"),
            ("Mix", "delay_mix")
        ]
    )