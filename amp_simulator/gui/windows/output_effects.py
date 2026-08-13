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

        # Checkbox and knobs in horizontal row
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

    # Output Effects UI
    dpg.add_text("Output Effect Controls")

    dpg.add_separator()

    # Reverb
    add_effect(
        "Reverb",
        "reverb_enabled",
        [
            ("Decay", "reverb_decay"),
            ("Damping", "reverb_damping"),
            ("Mix", "reverb_mix")
        ]
    )

    # Limiter
    add_effect(
        "Limiter",
        "limiter_enabled",
        [
            ("Ceiling", "limiter_ceiling"),
            ("Release", "limiter_release")
        ]
    )

    # Master Volume
    dpg.add_text("Master Volume")

    with dpg.group(horizontal=True):
        add_knob(
            "Volume",
            "master_volume"
        )

    dpg.add_separator()