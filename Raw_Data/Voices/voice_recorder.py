import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import keyboard
import time

def record_audio(filename, duration=5, fs=16000):
    print(f"Recording {filename}...")                                                                                             
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    
    for remaining in range(duration, 0, -1):
        print(f"Recording... {remaining} seconds remaining", end='\r')
        time.sleep(1)
    
    sd.wait()
    wav.write(filename, fs, recording)
    print(f"\nAudio recorded and saved as {filename}")
    return filename

if __name__ == "__main__":
    for i in range(1, 21):
        print(f"Press spacebar to start recording sample{i}.wav")
        keyboard.wait('space')
        filename = f"Raw_Data/Voices/sample{i}.wav"
        record_audio(filename)