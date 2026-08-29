import numpy as np
from ..core.filters import OnePoleFilter

class DelayLine:
    def __init__(self, delay_samples):
        self.delay_samples = delay_samples
        self.buffer = np.zeros(delay_samples)
        self.write_index = 0
        self.filter = OnePoleFilter()

    def process_sample(self, sample, feedback, absorption):
        read_index = self.write_index
        delayed = self.buffer[read_index]
        
        filtered = self.filter.process_sample(delayed, absorption)
        feedback_signal = filtered * feedback # decay is mapped to feedback when passed from reverb
        
        self.buffer[self.write_index] = sample + feedback_signal
        
        self.write_index = (self.write_index + 1) % self.delay_samples
        
        return delayed

    def reset(self):
        self.buffer.fill(0.0)
        self.write_index = 0
        self.filter.reset() 

class Reverb:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

        # Simulates the time it takes for sound to reach the first wall.
        self.pre_delay_ms = 24.0
        self.pre_delay_samples = int(self.pre_delay_ms * sample_rate / 1000.0)
        self.pre_delay_buffer = np.zeros(self.pre_delay_samples)
        self.pre_delay_write_index = 0

        # Irregular delay lengths prevent periodic echo patterns and reduce metallic resonances.
        delay_times_ms = [29, 37, 43, 53]

        self.delay_lines = []
        for delay_ms in delay_times_ms:
            delay_samples = int(delay_ms * sample_rate / 1000.0)
            self.delay_lines.append(DelayLine(delay_samples))

    def process(self, x, params):
        decay = self.map_knob(params.reverb_decay, 0.4, 0.85)
        absorption = self.map_knob(params.reverb_damping, 0.1, 0.9)
        mix = self.map_knob(params.reverb_mix, 0.0, 1.0)

        wet = np.zeros_like(x)

        for i, sample in enumerate(x):

            pre_delayed_sample = self.pre_delay_buffer[self.pre_delay_write_index]
            self.pre_delay_buffer[self.pre_delay_write_index] = sample
            
            self.pre_delay_write_index = (self.pre_delay_write_index + 1) % self.pre_delay_samples

            reflection_sum = 0.0

            # Feed the PRE-DELAYED sample into all parallel delay lines
            for delay in self.delay_lines:
                reflection = delay.process_sample(pre_delayed_sample, decay, absorption)
                reflection_sum += reflection

            # Average the output to prevent volume spikes
            wet[i] = reflection_sum / len(self.delay_lines)

        y = ((1.0 - mix) * x) + (mix * wet)

        return y

    @staticmethod
    def map_knob(value, out_min, out_max):
        value = np.clip(float(value), 0.0, 10.0)
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        # Reset pre-delay
        self.pre_delay_buffer.fill(0.0)
        self.pre_delay_write_index = 0
        
        # Reset parallel lines
        for delay in self.delay_lines:
            delay.reset()