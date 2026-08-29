# Python Guitar Amp Simulator

A real-time virtual guitar amplifier built in Python using digital signal processing (DSP). The project recreates the signal-processing stages of a guitar amplifier and several common guitar effects entirely in software.

## Full Technical Documentation

**[Watch the full project documentation on YouTube](https://youtu.be/FD1MlE2VeUg)**

The video provides a much more comprehensive look at the project than this README, including the architecture, DSP concepts, design decisions, implementation details, and reasoning behind each processing stage.

## Features

The amplifier currently includes:

* **Noise Gate**
* **Compressor**
* **Overdrive**
* **Chorus**
* **Delay**
* **Three-Band EQ**
* **Cabinet Impulse Response (IR) Convolution**
* **Reverb**
* **Limiter**

The application also provides a graphical interface for controlling the amplifier and includes waveform and frequency-spectrum visualizations for analyzing the processed audio.

## DSP Signal Chain

The audio is processed through three main stages: input stage, amp stage, and output stage

```text
Input Stage
    ↓
Noise Gate
    ↓
Compressor
    ↓
Overdrive
    ↓
Chorus
    ↓
Delay
    ↓
Amp Stage
    ↓
Three-Band EQ
    ↓
Cabinet IR
    ↓
Output Stage
    ↓
Reverb
    ↓
Limiter
    ↓
Audio Output
```

The project implements the individual effects using DSP techniques such as IIR filtering, nonlinear waveshaping, delay lines, interpolation, convolution, envelope following, and frequency-domain analysis.

## Project Structure

```text
amp_simulator/
├── __init__.py
├── main.py
│
├── app/
│   ├── __init__.py
│   ├── context.py
│   └── state/
│       ├── __init__.py
│       ├── params.py
│       ├── audio_config.py
│       └── analysis.py
│
├── audio_dsp/
│   ├── __init__.py
│   ├── audio_engine.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── filters.py
│   │   ├── eq.py
│   │   └── cabinet.py
│   │
│   ├── effects/
│   │   ├── __init__.py
│   │   ├── noise_gate.py
│   │   ├── compressor.py
│   │   ├── overdrive.py
│   │   ├── chorus.py
│   │   ├── delay.py
│   │   ├── reverb.py
│   │   └── limiter.py
│   │
│   └── irs/
│       ├── README.md
│       └── *.wav
│
└── gui/
    ├── __init__.py
    ├── gui.py
    ├── components/
    │   └── ...
    └── windows/
        ├── main_amp.py
        ├── input_effects.py
        ├── amp_effects.py
        ├── output_effects.py
        ├── analysis.py
        └── settings.py
```

The application is organized into separate GUI, application-state, audio-engine, and DSP components. The `AppContext` connects these components and provides shared access to the application's state and processing objects.

## Requirements

* Python 3.11+ recommended
* An audio input device
* An audio output device
* A guitar and audio interface for guitar input (though microphone input can be processed aswell)

The application processes audio at **48 kHz**. (Sampling rate can be altered in settings tab, but 48 kHz is recommended.)

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd guitar_amp_simulator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

From the repository root, run:

```bash
python -m amp_simulator.main
```

The application should open the graphical interface and begin processing audio through the configured input and output devices.

## Audio Configuration

The application requires an input and output audio device. The devices are configured through the application's audio configuration.

For the intended setup, a guitar is connected to an audio interface, which provides the digitized guitar signal to the application:

```text
Guitar
   ↓
Audio Interface
   ↓
Python DSP
   ↓
Audio Interface
   ↓
Headphones / Speakers
```

For real-time guitar processing, using an audio interface with headphones connected to the interface is recommended to minimize latency.

## Cabinet Impulse Responses

The project includes cabinet impulse responses from **Jester Dyne Productions' Brutal IR Pack**.

The included 48 kHz impulse responses are used by the cabinet convolution stage to simulate the frequency response of a guitar speaker cabinet.

See [`amp_simulator/audio_dsp/irs/README.md`](amp_simulator/audio_dsp/irs/README.md) for information about the included impulse responses and their licensing.

## Documentation

The most comprehensive documentation of this project is the accompanying YouTube video.

It covers:

* Application architecture
* File organization
* GUI implementation
* Audio engine
* DSP fundamentals
* Individual effect implementations
* Design decisions
* Implementation decisions
* Processing algorithms
* Project development and lessons learned

**[Watch the full technical documentation](https://youtu.be/FD1MlE2VeUg)**

## License

The source code for this project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for the complete license.

Third-party assets, including the cabinet impulse responses, are subject to their respective licenses. See the documentation in the `irs` directory for details.
