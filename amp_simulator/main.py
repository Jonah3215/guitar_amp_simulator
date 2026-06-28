from params import Params
from audio_engine import start_audio
# from gui import start_gui

# in place of "start_gui" you can name it whatever you want (it's up to you)

def main(): 
    # params will be an instance of Params, holding all the parameters to be used throughout
    params = Params()

    # starts the real-time audio processing; parametrized by params
    start_audio(params)

    # starts the graphical interface; runs until window is closed by user
    # start_gui(params)
    # uncomment and call when we get a working GUI setup
        
if __name__ == "__main__":
    main()