import sounddevice as sd
from dsp import process

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
        outdata[:, 0] = y

    # create audio stream
    # samplerate = 44.1 kHz
    stream = sd.Stream(
        samplerate = 44100,
        blocksize = 256,
        channels = 1,
        dtype = 'float32',
        callback = callback
    )

    # start real-time audio processing
    stream.start()

    return stream