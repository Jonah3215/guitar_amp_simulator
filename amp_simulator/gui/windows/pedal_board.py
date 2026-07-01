import dearpygui.dearpygui as dpg


def create_tab(params):

    dpg.add_text("Pedal Board")

    dpg.add_separator()

    dpg.add_checkbox(label="Overdrive")

    dpg.add_checkbox(label="Chorus")

    dpg.add_checkbox(label="Delay")

    dpg.add_checkbox(label="Reverb")