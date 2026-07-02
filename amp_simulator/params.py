class Params:
    def __init__(self):
        # all parameters take on values [0, 10]
        # core amp controls
        self.gain = 5.0
        self.drive = 2.0
        self.volume = 5.0

        # eq knobs
        self.bass = 5.0
        self.mid = 5.0
        self.treble = 5.0

        # distortion pedal (NOT used in first run)
        # self.distortion_on = False
        # self.distortion_amount = 5.0

        # delay pedal (NOT used in first run)
        # self.delay_on = False
        # self.delay_time = 5.0
        # self.delay_mix = 5.0

        # reverb pedal (NOT used in first run)
        # self.reverb_on = False
        # self.reverb_mix = 5.0

        # chorus pedal (NOT used in first run)
        # self.chorus_on = False
        # self.chorus_depth = 5.0
        # self.chorus_rate = 5.0