import dearpygui.dearpygui as dpg

from .windows.input_effects import create_tab as create_pedal_board
from .windows.main_amp import create_tab as create_main_amp
from .windows.output_effects import create_tab as create_out_effects
from .windows.analysis import create_tab as create_analytics_viewer
from .windows.settings import create_tab as create_settings


def start_gui(app):
    dpg.create_context()

    dpg.create_viewport(
        title="Amp Simulator",
        width=1000,
        height=600
    )

    with dpg.window(
        label="Amp Simulator",
        width=985,
        height=560,
        no_close=True,
        no_resize=True,
        no_move=True,
    ):

        with dpg.tab_bar():

            with dpg.tab(label="Main Amp"):
                create_main_amp(app)

            with dpg.tab(label="Input Effects"):
                create_pedal_board(app)

            with dpg.tab(label="Output Effects"):
                create_out_effects(app)

            with dpg.tab(label="Analytics"):
                create_analytics_viewer(app)

            with dpg.tab(label="Settings"):
                create_settings(app)


    dpg.setup_dearpygui()
    dpg.show_viewport()


    # Main GUI loop
    while dpg.is_dearpygui_running():

        # Update plots at GUI refresh rate
        if hasattr(app, "update_analysis"):
            app.update_analysis()

        dpg.render_dearpygui_frame()


    dpg.destroy_context()