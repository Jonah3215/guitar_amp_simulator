from amp_simulator.params import Params
from amp_simulator.audio_engine import start_audio
from amp_simulator.gui.gui import start_gui

def main(): 
    # params will be an instance of Params, holding all the parameters to be used throughout
    params = Params()

    # starts the real-time audio processing; parametrized by params
    start_audio(params)

    # starts the gui, modified params; runs until window is closed by user
    start_gui(params)
        
if __name__ == "__main__":
    main()


    # test
    # hey man