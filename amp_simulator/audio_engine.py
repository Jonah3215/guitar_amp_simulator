import sounddevice as sd
from amp_simulator.dsp.process import process

def start_audio(app):
    def callback(indata, outdata, frames, time, status):

        if status:
            print(status)

        x = indata[:, 0]

        y = process(x, app)

        outdata[:, 0] = y
        outdata[:, 1] = y

    stream = sd.Stream(
        samplerate=app.sample_rate,
        blocksize=app.block_size,
        dtype="float32",
        #device=(14, 13),
        channels=2,
        callback=callback
    )

    stream.start()
    app.audio_stream = stream

    return stream