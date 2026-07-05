import os

from amp_simulator.dsp.cabinet import CabinetIR
from amp_simulator.dsp.eq import ThreeBandEQ
from amp_simulator.params import Params

class AppContext:
    def __init__(self):
        # user parameters (knobs)
        self.params = Params()

        # stateful DSP objects
        self.cabinet = CabinetIR()
        self.eq = ThreeBandEQ()

        # IR list
        self.ir_list = [
            os.path.join("irs", f)
            for f in os.listdir("irs")
            if f.lower().endswith(".wav")
        ]

        # system config
        self.sample_rate = 48000
        self.block_size = 256

        # audio stream handle
        self.audio_stream = None