import dearpygui.dearpygui as dpg


def create_tab(app):

    analysis = app.analysis


    dpg.add_text("Signal Analysis")
    dpg.add_separator()


    # ============================================================
    # DRY WAVEFORM
    # ============================================================

    dpg.add_text("Dry Waveform")

    with dpg.plot(
        label="Dry Signal",
        height=250,
        width=700,
        no_mouse_pos=True,
        no_box_select=True,
        no_menus=True
    ):

        dpg.add_plot_axis(
            dpg.mvXAxis,
            label="Samples",
            tag="dry_waveform_x"
        )

        with dpg.plot_axis(
            dpg.mvYAxis,
            label="Amplitude",
            tag="dry_waveform_y"
        ):

            dpg.add_line_series(
                [],
                [],
                label="Dry",
                tag="dry_waveform"
            )


    dpg.set_axis_limits(
        "dry_waveform_y",
        -1.0,
        1.0
    )


    # ============================================================
    # WET WAVEFORM
    # ============================================================

    dpg.add_text("Wet Waveform")

    with dpg.plot(
        label="Wet Signal",
        height=250,
        width=700,
        no_mouse_pos=True,
        no_box_select=True,
        no_menus=True
    ):

        dpg.add_plot_axis(
            dpg.mvXAxis,
            label="Samples",
            tag="wet_waveform_x"
        )

        with dpg.plot_axis(
            dpg.mvYAxis,
            label="Amplitude",
            tag="wet_waveform_y"
        ):

            dpg.add_line_series(
                [],
                [],
                label="Wet",
                tag="wet_waveform"
            )


    dpg.set_axis_limits(
        "wet_waveform_y",
        -1.0,
        1.0
    )


    dpg.add_separator()

    dpg.add_text("Spectrum Analyzer")


    # ============================================================
    # SPECTRUM
    # ============================================================

    with dpg.plot(
        label="Frequency Spectrum",
        height=300,
        width=700,
        no_mouse_pos=True,
        no_box_select=True,
        no_menus=True,
        tag="spectrum_plot"
    ):

        dpg.add_plot_legend()

        dpg.add_plot_axis(
            dpg.mvXAxis,
            label="Frequency (Hz)",
            tag="spectrum_x"
        )

        with dpg.plot_axis(
            dpg.mvYAxis,
            label="dB",
            tag="spectrum_y"
        ):

            dpg.add_line_series(
                [],
                [],
                label="Dry Spectrum",
                tag="dry_spectrum"
            )

            dpg.add_line_series(
                [],
                [],
                label="Wet Spectrum",
                tag="wet_spectrum"
            )


    # Spectrum always starts at origin
    dpg.set_axis_limits(
        "spectrum_x",
        0,
        app.config.sample_rate / 2
    )

    dpg.set_axis_limits(
        "spectrum_y",
        -120,
        40
    )

    # ============================================================
    # UPDATE FUNCTION
    # ============================================================

    def update_analysis():
        # ----------------------------
        # Waveforms
        # ----------------------------

        if analysis.dry_waveform.size > 0:

            waveform_x = list(
                range(len(analysis.dry_waveform))
            )


            dpg.set_value(
                "dry_waveform",
                [
                    waveform_x,
                    analysis.dry_waveform.tolist()
                ]
            )

            dpg.set_value(
                "wet_waveform",
                [
                    waveform_x,
                    analysis.wet_waveform.tolist()
                ]
            )


            # Dynamically update x-axis
            dpg.set_axis_limits(
                "dry_waveform_x",
                0,
                len(waveform_x)
            )

            dpg.set_axis_limits(
                "wet_waveform_x",
                0,
                len(waveform_x)
            )


        # ----------------------------
        # Spectrum
        # ----------------------------

        if ((analysis.frequencies.size > 0)
        and (analysis.dry_spectrum.size > 0)
        and (analysis.wet_spectrum.size > 0)):

            dpg.set_value(
                "dry_spectrum",
                [
                    analysis.frequencies.tolist(),
                    analysis.dry_spectrum.tolist()
                ]
            )

            dpg.set_value(
                "wet_spectrum",
                [
                    analysis.frequencies.tolist(),
                    analysis.wet_spectrum.tolist()
                ]
            )


            # Update frequency axis if sample rate changes
            dpg.set_axis_limits(
                "spectrum_x",
                0,
                analysis.frequencies[-1]
            )

    print("Analysis tab initialized")
    app.update_analysis = update_analysis