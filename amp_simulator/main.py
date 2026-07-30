from amp_simulator.app.app_context import AppContext
from amp_simulator.gui.gui import start_gui

def main():
    app = AppContext()
    
    app.audio_engine.start()

    start_gui(app)

if __name__ == "__main__":
    main()