class Params:
    def __init__(self):
        # all parameters take on values [0, 10]
        # core amp controls
        self.gain = 5.0
        self.drive = 2.0
        self.volume = 5.0

        # eq knobs
        self.bass = 5.0
        self.mids = 5.0
        self.treble = 5.0

        # cabinet IR controls
        self.ir_enabled = False
        self.selected_ir = 0

        # noise gate
        self.noise_gate_enabled = False
        self.noise_gate_threshold = 5.0
        self.noise_gate_attack = 5.0
        self.noise_gate_decay = 5.0
        
        # compressor
        self.compressor_enabled = False
        self.compressor_threshold = 6.0
        self.compressor_ratio = 2.5
        self.compressor_attack = 7.0
        self.compressor_decay = 5.0
        self.compressor_makeup = 1.5

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