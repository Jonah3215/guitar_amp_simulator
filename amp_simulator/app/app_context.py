import os

from amp_simulator.app.state.params import Params
from amp_simulator.app.state.audio_config import AudioConfig
from amp_simulator.app.state.analysis import Analysis

from amp_simulator.audio_dsp.audio_engine import AudioEngine

from amp_simulator.audio_dsp.effects.noise_gate import NoiseGate
from amp_simulator.audio_dsp.effects.compressor import Compressor
from amp_simulator.audio_dsp.effects.overdrive import Overdrive
from amp_simulator.audio_dsp.effects.chorus import Chorus
from amp_simulator.audio_dsp.effects.delay import Delay

from amp_simulator.audio_dsp.core.cabinet import CabinetIR
from amp_simulator.audio_dsp.core.eq import ThreeBandEQ

from amp_simulator.audio_dsp.effects.reverb import Reverb
from amp_simulator.audio_dsp.effects.limiter import Limiter

"""
This module contains centralizes all stateful information 
through the App Context Class

AppContext acts as the glue layer between UI and DSP
"""

class AppContext:
    def __init__(self):
        self.config = AudioConfig()
        self.params = Params()
        self.analysis = Analysis()

        # input stage objects
        self.noise_gate = NoiseGate(self.config.sample_rate)
        self.compressor = Compressor()
        self.overdrive = Overdrive()
        self.chorus = Chorus(self.config.sample_rate)
        self.delay = Delay(self.config.sample_rate)

        # amp stage objects
        self.cabinet = CabinetIR(self.config.block_size)
        self.eq = ThreeBandEQ()

        # output stage objects
        self.reverb = Reverb(self.config.sample_rate)
        self.limiter = Limiter()

        # dynmically create IR list
        ir_folder = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "audio_dsp",
                "irs"
            )
        )

        self.ir_list = [
            os.path.join(ir_folder, f)
            for f in os.listdir(ir_folder)
            if f.lower().endswith(".wav")
        ]

        # Load the first cabinet IR if one is available
        if self.ir_list:
            self.cabinet.load_ir(self.ir_list[0])

        # audio stream handle
        self.audio_engine = AudioEngine(self)
