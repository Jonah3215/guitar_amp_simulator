import numpy as np

class OnePoleFilter:
    def __init__(self):
        self.y = 0.0

    def process_sample(self, x, a):
        # processes a single sample
        self.y = (1 - a) * x + a * self.y
        return self.y

    def process(self, x, a):
        # processes an array of samples
        y = np.zeros_like(x)
        a_clipped = np.clip(a, 0.0, 0.999)

        for i in range(len(x)):
            y[i] = self.process_sample(x[i], a_clipped)

        return y

    def reset(self):
        self.y = 0.0


class OnePoleHighPass:
    def __init__(self):
        self.x_prev = 0.0
        self.y = 0.0

    def process_sample(self, x, a):
        # processes a single sample
        self.y = a * (self.y + x - self.x_prev)
        self.x_prev = x
        return self.y

    def process(self, x, a):
        # processes an array of samples
        y = np.zeros_like(x)
        a_clipped = np.clip(a, 0.0, 0.999)

        for i in range(len(x)):
            y[i] = self.process_sample(x[i], a_clipped)

        return y

    def reset(self):
        self.x_prev = 0.0
        self.y = 0.0