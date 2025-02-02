import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import keyboard

def record_audio(filename, duration=5, fs=16000):
    print(f"Recording {filename}...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, recording)
    print(f"Audio recorded and saved as {filename}")
    return filename

def transcribe_audio(audio_path, model_size="base"):
    print("Loading Whisper model...")
    model = whisper.load_model(model_size)
    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    transcription = result["text"]
    print("Transcription complete.")
    
    # Save transcription to a text file
    transcript_filename = audio_path.replace(".wav", ".txt").replace("voice/", "text/")
    with open(transcript_filename, "w", encoding="utf-8") as file:
        file.write(transcription)
    print(f"Transcription saved as {transcript_filename}")
    
    return transcription

if __name__ == "__main__":
    filename = "Output/voice/" + input("Enter the name for the WAV file (without extension): ") + ".wav"
    print("Press spacebar to start recording...")
    keyboard.wait('space')
    record_audio(filename, duration=5)
    transcription = transcribe_audio(filename)
    print(f"Transcribed Text for {filename}: {transcription}")