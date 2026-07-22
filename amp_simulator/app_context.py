import os
from amp_simulator.params import Params

from amp_simulator.dsp.effects.noise_gate import NoiseGate
from amp_simulator.dsp.effects.compressor import Compressor

from amp_simulator.dsp.core.cabinet import CabinetIR
from amp_simulator.dsp.core.eq import ThreeBandEQ

class AppContext:
    def __init__(self):
        # user parameters (knobs)
        self.params = Params()

        # stateful DSP objects
        self.cabinet = CabinetIR()
        self.eq = ThreeBandEQ()
        self.noise_gate = NoiseGate()
        self.compressor = Compressor()

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