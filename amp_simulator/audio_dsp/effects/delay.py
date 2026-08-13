import numpy as np

class Delay:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

        self.max_delay_ms = 1000.0
        self.buffer_size = int(self.sample_rate * (self.max_delay_ms / 1000.0))
        
        self.buffer = np.zeros(self.buffer_size)
        self.write_index = 0

    def process(self, x, params):
        # map GUI knobs
        delay_ms = self.map_knob(params.delay_time, 50.0, 800.0) # [50, 800] ms
        feedback = self.map_knob(params.delay_feedback, 0.0, 0.95) 
        mix = self.map_knob(params.delay_mix, 0.0, 1.0)

        # convert milliseconds to samples. 
        delay_samples = int(delay_ms * (self.sample_rate / 1000.0))
        
        delay_samples = np.clip(delay_samples, 1, self.buffer_size - 1)

        y = np.zeros_like(x)

        for i, sample in enumerate(x):
            read_pos = (self.write_index - delay_samples) % self.buffer_size
            
            delayed_sample = self.buffer[read_pos]

            # mix dry and wet signals for the output
            y[i] = (1.0 - mix) * sample + (mix * delayed_sample)

            # write current sample + feedback * delayed_sample
            new_buffer_val = sample + (feedback * delayed_sample)
            self.buffer[self.write_index] = new_buffer_val

            self.write_index = (self.write_index + 1) % self.buffer_size

        return y

    @staticmethod
    def map_knob(value, out_min, out_max):
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        self.buffer.fill(0.0)
        self.write_index = 0