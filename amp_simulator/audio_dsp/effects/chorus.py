import numpy as np

class Chorus:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.center_delay_ms = 20.0 

        max_delay_ms = 50.0

        self.buffer_size = int(sample_rate * (max_delay_ms / 1000.0))
        self.buffer = np.zeros(self.buffer_size)

        self.write_index = 0
        self.phase = 0.0

    def process(self, x, params):
        rate = self.map_knob(params.chorus_rate, 0.1, 5.0)
        depth = self.map_knob(params.chorus_depth, 0.0, 10.0)
        mix = self.map_knob(params.chorus_mix, 0.0, 1.0)

        y = np.zeros_like(x)

        phase_increment = 2.0 * np.pi * rate / self.sample_rate

        for i, sample in enumerate(x):
            self.buffer[self.write_index] = sample

            # Generate LFO value [-1.0 to 1.0] and advance phase
            lfo_val = np.sin(self.phase)
            self.phase = (self.phase + phase_increment) % (2.0 * np.pi)

            delay_ms = self.center_delay_ms + (depth * lfo_val)

            delay_samples = delay_ms * (self.sample_rate / 1000.0)
            delay_samples = np.clip(delay_samples, 1, self.buffer_size - 2)

            read_pos = (self.write_index - delay_samples) % self.buffer_size

            # Read delayed sample (use interpolation for fractional delays)
            delayed_sample = self.interpolate(read_pos)

            y[i] = (1.0 - mix) * sample + (mix * delayed_sample)

            self.write_index = (self.write_index + 1) % self.buffer_size

        return y

    def interpolate(self, position):
        idx1 = int(np.floor(position))
        idx2 = (idx1 + 1) % self.buffer_size
        
        frac = position - idx1
        
        # Blend samples based on proximity
        return (1.0 - frac) * self.buffer[idx1] + (frac * self.buffer[idx2])

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        # Clear delay buffer to prevent old noise from bleeding into new playback
        self.buffer.fill(0.0)
        self.write_index = 0
        self.phase = 0.0