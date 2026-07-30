class Params:
    def __init__(self):
        # all parameters take on values [0, 10] or (True / False)
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

        # overdrive
        self.overdrive_enabled = False
        self.overdrive_drive = 5.0
        self.overdrive_tone = 5.0
        self.overdrive_level = 5.0

        # chorus
        self.chorus_enabled = False
        self.chorus_rate = 3.0
        self.chorus_depth = 5.0
        self.chorus_mix = 5.0

        # delay
        self.delay_enabled = False
        self.delay_time = 5.0
        self.delay_feedback = 3.0
        self.delay_mix = 3.0

        # reverb
        self.reverb_enabled = False
        self.reverb_decay = 5.0
        self.reverb_damping = 5.0
        self.reverb_mix = 3.0

        # output
        self.master_volume = 8.0

        # limiter
        self.limiter_enabled = False
        self.limiter_ceiling = 9.0
        self.limiter_release = 5.0