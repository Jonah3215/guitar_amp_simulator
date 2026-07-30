class AudioConfig:
    def __init__(self):
        # all elements used in the settings menu
        self.sample_rate = 48000
        self.block_size = 256

        self.input_device = None
        self.output_device = None