import sounddevice as sd
from amp_simulator.dsp.dsp import process

INPUT_DEVICE = 14 # 14 Analogue 1 + 2 (Focusrite USB Audio), WASAPI (2 in, 0 out)
OUTPUT_DEVICE = 13 # 13 Speakers (Focusrite USB Audio), WASAPI (0 in, 2 out)

def start_audio(params):
    # sets up the real-time audio stream
    def callback(indata, outdata, frames, time, status):
        # indata = incoming audio buffer, the guitar signal
        # outdata = buffer we must fill for output

        if status:
            print(status)

        # take first channel (mono guitar input)
        x = indata[:, 0]

        # send through DSP chain
        y = process(x, params)

        # write processed signal to output
        outdata[:, 0] = y  # left ear
        outdata[:, 1] = y  # right ear

    # create audio stream
    # this assumes a sample rate of 48 kHz
    # if you're using this change your interfacing sample rate
    # or change the sample rate parameter value
    stream = sd.Stream(
        samplerate=48000,
        blocksize=256,
        dtype='float32',
        # device=(INPUT_DEVICE, OUTPUT_DEVICE),
        channels=(1, 2),
        callback=callback
    )

    # start real-time audio processing
    stream.start()

    return stream