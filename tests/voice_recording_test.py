import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

def record_audio(filename="tests/test_outputs/test_audio.wav", duration=5, fs=16000):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, recording)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    record_audio()