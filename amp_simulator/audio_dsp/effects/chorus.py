import numpy as np

class Chorus:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.center_delay_ms = 20.0 

        # Optimize: Size buffer to slightly larger than the max possible delay (e.g., 50ms)
        # This saves memory and prevents cache misses compared to a 1-second buffer.
        max_delay_ms = 50.0
        self.buffer_size = int(sample_rate * (max_delay_ms / 1000.0))
        self.buffer = np.zeros(self.buffer_size)

        self.write_index = 0
        self.phase = 0.0

    def process(self, x, params):
        # Rate: 0.1Hz (slow sweep) to 5.0Hz (fast vibrato wobble)
        rate = self.map_knob(params.chorus_rate, 0.1, 5.0)
        # Depth: 0.0ms (no movement) to 10.0ms (heavy detuning)
        depth = self.map_knob(params.chorus_depth, 0.0, 10.0)
        mix = self.map_knob(params.chorus_mix, 0.0, 1.0)

        y = np.zeros_like(x)

        phase_increment = 2.0 * np.pi * rate / self.sample_rate

        for i, sample in enumerate(x):
            # Write current sample into delay buffer
            self.buffer[self.write_index] = sample

            # Generate LFO value (-1.0 to 1.0) and advance phase
            lfo_val = np.sin(self.phase)
            self.phase = (self.phase + phase_increment) % (2.0 * np.pi)

            # Calculate current delay time (oscillates around center_delay_ms)
            delay_ms = self.center_delay_ms + (depth * lfo_val)

            # Convert delay from ms to samples
            delay_samples = delay_ms * (self.sample_rate / 1000.0)

            # Ensure delay is strictly within our buffer limits.
            delay_samples = np.clip(delay_samples, 1, self.buffer_size - 2)

            # Calculate read position using circular buffer
            read_pos = (self.write_index - delay_samples) % self.buffer_size

            # Read delayed sample (use interpolation for fractional delays)
            delayed_sample = self.interpolate(read_pos)

            y[i] = (1.0 - mix) * sample + (mix * delayed_sample)

            # Move write pointer forward and wrap around
            self.write_index = (self.write_index + 1) % self.buffer_size

        return y

    def interpolate(self, position):
        # Find lower index (integer below)
        idx1 = int(np.floor(position))
        
        # Find upper index (wrapped to buffer bounds)
        idx2 = (idx1 + 1) % self.buffer_size
        
        # Find fractional distance between the two indices
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