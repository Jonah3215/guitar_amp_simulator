import dearpygui.dearpygui as dpg

# This is here just for the sake of learning what this would even look like
# Lots of effort must be expended here to make this actually function (I assume at least)

def create_tab(params):

    dpg.add_text("Waveform Viewer")

    with dpg.plot(height=450, width=-1):

        dpg.add_plot_legend()

        dpg.add_plot_axis(dpg.mvXAxis, label="Time")

        y_axis = dpg.add_plot_axis(
            dpg.mvYAxis,
            label="Amplitude"
        )

        dpg.add_line_series([], [], parent=y_axis)