import numpy as np
from ..core.filters import OnePoleFilter

class DelayLine:
    def __init__(self, delay_samples):
        self.delay_samples = delay_samples
        
        # Circular buffer to hold the delay history.
        self.buffer = np.zeros(delay_samples)
        
        # Write pointer tracks where we are currently recording into the buffer
        self.write_index = 0
        
        # A single-pole low-pass filter simulates the way high frequencies 
        # are absorbed by walls/air faster than low frequencies.
        self.filter = OnePoleFilter()

    def process_sample(self, sample, feedback, absorption):
        # Read delayed sample from the buffer
        read_index = self.write_index
        delayed = self.buffer[read_index]
        
        # Filter delayed sample for the feedback path
        # 'absorption' acts as our filter coefficient (higher = darker/more absorbed)
        filtered = self.filter.process_sample(delayed, absorption)
        
        # Apply feedback to the filtered sample
        feedback_signal = filtered * feedback
        
        # Write input + feedback signal into buffer
        self.buffer[self.write_index] = sample + feedback_signal
        
        # Advance write pointer and wrap around
        self.write_index = (self.write_index + 1) % self.delay_samples
        
        # We return the purely delayed sample for the output mix
        return delayed

    def reset(self):
        self.buffer.fill(0.0)
        self.write_index = 0
        self.filter.reset()

 
class Reverb:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate

        # Simulates the time it takes for sound to reach the first wall.
        # 24ms gives a nice sense of acoustic space without feeling like a distinct slapback echo.
        self.pre_delay_ms = 24.0
        self.pre_delay_samples = int(self.pre_delay_ms * sample_rate / 1000.0)
        self.pre_delay_buffer = np.zeros(self.pre_delay_samples)
        self.pre_delay_write_index = 0

        # Irregular delay lengths prevent periodic echo patterns
        # and reduce metallic resonances.
        delay_times_ms = [
            29,
            37,
            43,
            53
        ]

        self.delay_lines = []
        for delay_ms in delay_times_ms:
            delay_samples = int(delay_ms * sample_rate / 1000.0)
            self.delay_lines.append(DelayLine(delay_samples))

    def process(self, x, params):
        # Map GUI parameters
        # Decay range reduced to 0.4 - 0.85 to prevent infinite volume stacking
        decay = self.map_knob(params.reverb_decay, 0.4, 0.85)
        
        # Damping mapped to absorption (0.1 = bright room, 0.9 = dark room)
        absorption = self.map_knob(params.reverb_damping, 0.1, 0.9)
        mix = self.map_knob(params.reverb_mix, 0.0, 1.0)

        wet = np.zeros_like(x)

        # Process the block sample-by-sample
        for i, sample in enumerate(x):
            
            # Read the oldest sample from the pre-delay buffer
            pre_delayed_sample = self.pre_delay_buffer[self.pre_delay_write_index]
            
            # Write the new dry sample into the pre-delay buffer
            self.pre_delay_buffer[self.pre_delay_write_index] = sample
            
            # Advance pre-delay pointer
            self.pre_delay_write_index = (self.pre_delay_write_index + 1) % self.pre_delay_samples

            reflection_sum = 0.0

            # Feed the PRE-DELAYED sample into all parallel delay lines
            for delay in self.delay_lines:
                reflection = delay.process_sample(pre_delayed_sample, decay, absorption)
                reflection_sum += reflection

            # Average the output to prevent volume spikes
            wet[i] = reflection_sum / len(self.delay_lines)

        # Dry/wet mix
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