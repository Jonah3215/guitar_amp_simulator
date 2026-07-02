# common filters that are used throughout the rest of the program

import numpy as np

class OnePoleLowPass:
    # to process the first input (since we need x[n] and y[n - 1])
    def __init__(self):
        self.y = 0.0 # y[n - 1] = 0

    def process(self, x, cutoff):
        # cutoff: 0.0 => bright; 1.0 => dark

        y = np.zeros_like(x)
        a = np.clip(cutoff, 0.0, 0.999)

        for i in range(len(x)):
            self.y = (1 - a) * x[i] + a * self.y
            y[i] = self.y

        return y

class OnePoleHighPass:
    def __init__(self):
        self.lp = OnePoleLowPass()

    def process(self, x, cutoff):
        # high-pass = original signal - low-pass version
        low = self.lp.process(x, cutoff)
        return (x - low)