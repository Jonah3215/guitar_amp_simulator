import sounddevice as sd
import numpy as np

from amp_simulator.audio_dsp.stages.input_stage import input_stage
from amp_simulator.audio_dsp.stages.amp_stage import amp_stage
from amp_simulator.audio_dsp.stages.output_stage import output_stage

class AudioEngine:
    def __init__(self, app):
        self.app = app
        self.stream = None

        self.update_analysis_config()
        
    def start(self):
        def callback(indata, outdata, frames, time, status):
            x = indata[:, 0]

            y = self.process(x)

            # update waveform
            self.app.analysis.dry_waveform = x.copy()
            self.app.analysis.wet_waveform = y.copy()

            # dry fft
            dry_fft = np.abs(np.fft.rfft(x))
            self.app.analysis.dry_spectrum = (
                20 * np.log10(dry_fft + 1e-6)
            ) # magnitude -> dB

            # wet fft
            wet_fft = np.abs(np.fft.rfft(y))
            self.app.analysis.wet_spectrum = (
                20 * np.log10(wet_fft + 1e-6)
            ) # magnitude -> dB

            outdata[:, 0] = y
            outdata[:, 1] = y

        self.stream = sd.Stream(
            samplerate=self.app.config.sample_rate,
            blocksize=self.app.config.block_size,
            dtype="float32",
            device=(
                self.app.config.input_device,
                self.app.config.output_device
            ),
            channels=2,
            callback=callback
        )

        self.stream.start()
        return self.stream

    def process(self, x):
        # Ensure correct datatype
        x = x.astype(np.float32)

        # DSP chain
        x = input_stage(x, self.app)
        x = amp_stage(x, self.app)
        x = output_stage(x, self.app)

        return x

    def stop(self):
        if (self.stream is not None):
            self.stream.stop()
            self.stream.close()
            self.stream = None

    def restart(self):
        self.stop()
        self.update_analysis_config()
        self.start()
        
    def update_analysis_config(self):
        self.app.analysis.update_frequency_axis(
            self.app.config.sample_rate,
            self.app.config.block_size
        )