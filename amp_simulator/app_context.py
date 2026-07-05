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
        ir_folder = os.path.join(os.path.dirname(__file__), "dsp", "irs")

        self.ir_list = [
            os.path.join(ir_folder, f)
            for f in os.listdir(ir_folder)
            if f.lower().endswith(".wav")
        ]

        # system config
        self.sample_rate = 48000
        self.block_size = 256

        # audio stream handle
        self.audio_stream = None