from amp_simulator.app_context import AppContext
from amp_simulator.audio_engine import start_audio
from amp_simulator.gui.gui import start_gui

def main():
    # create shared application state
    app = AppContext()

    # load default cabinet IR
    app.cabinet.load_ir(app.ir_list[0])

    # start audio engine (real-time DSP)
    start_audio(app)

    # start GUI (user control layer)
    start_gui(app)

if __name__ == "__main__":
    main()