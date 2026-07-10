import dearpygui.dearpygui as dpg

from .windows.main_amp import create_tab as create_main_amp
from .windows.pedal_board import create_tab as create_pedal_board
from .windows.waveform_viewer import create_tab as create_waveform_viewer

def start_gui(app):
    params = app.params

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

            with dpg.tab(label="Pedal Board"):
                create_pedal_board(params)

            with dpg.tab(label="Waveform Viewer"):
                create_waveform_viewer(params)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()