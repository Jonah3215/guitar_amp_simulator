import numpy as np
from ..core.filters import OnePoleFilter

class Limiter:
    def __init__(self):
        # Envelope follower to track the volume of the incoming signal
        self.env_filter = OnePoleFilter()
        
        # Envelope smoothing coefficient (keeps the tracking stable, avoiding buzzing)
        self.env_coeff = 0.95 

        # Current gain multiplier (starts fully transparent at 1.0)
        self.gain = 1.0

        # Fixed fast attack coefficient.
        # 0.01 is extremely fast (relies 99% on the new target gain, 1% on the past).
        # A limiter must react almost instantly to prevent digital clipping.
        self.attack_coeff = 0.01

    def process(self, x, params):
        # Ceiling: Knob 0 -> -6 dB (safe/quiet), Knob 10 -> 0 dB (loud/max volume)
        ceiling_db = self.map_knob(params.limiter_ceiling, -6.0, 0.0)
        # Convert decibels to a linear amplitude threshold (0.0 to 1.0)
        ceiling = 10.0 ** (ceiling_db / 20.0)
        release_coeff = self.map_knob(params.limiter_release, 0.99, 0.9999)

        y = np.zeros_like(x)

        # Process sample-by-sample
        for i, sample in enumerate(x):
            
            # Measure envelope (rectify the wave by taking the absolute value, then smooth it)
            envelope = self.env_filter.process_sample(abs(sample), self.env_coeff)

            # Compute target gain using helper method
            target_gain = self.compute_gain(envelope, ceiling)

            # Choose attack or release coefficient
            # If target_gain is lower than current gain, a peak hit and we must ATTACK (reduce volume).
            if target_gain < self.gain:
                coeff = self.attack_coeff
            else:
                # Otherwise, the peak has passed and we can gradually RELEASE (restore volume).
                coeff = release_coeff

            # Smooth the gain change so it doesn't cause audible clicking
            self.gain = (1.0 - coeff) * target_gain + coeff * self.gain

            # Apply the gain reduction to the actual audio sample
            y[i] = sample * self.gain

        return y

    def compute_gain(self, envelope, ceiling):
        # If the envelope is below our ceiling (or effectively silent), leave gain at 1.0
        if envelope <= ceiling or envelope < 1e-6:
            return 1.0
            
        # If the envelope exceeds the ceiling, calculate the exact fraction needed 
        # to squash the envelope down to the ceiling limit, clamped for safety.
        return np.clip(ceiling / envelope, 0.0, 1.0)

    @staticmethod
    def map_knob(value, out_min, out_max):
        # Protect math from out-of-bounds UI slider values
        value = np.clip(float(value), 0.0, 10.0)
        return out_min + (value / 10.0) * (out_max - out_min)

    def reset(self):
        # Clear filter memory and restore full volume when switching presets
        self.env_filter.reset()
        self.gain = 1.0