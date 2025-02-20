import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import keyboard
from langdetect import detect
from googletrans import Translator

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
    
    return transcription, transcript_filename

def detect_and_translate(text):
    translator = Translator()
    detected_language = detect(text)
    language = "na"
    
    if detected_language == 'en':
        translated = translator.translate(text, src='en', dest='de').text
        language = "de_Translated"
    elif detected_language == 'de':
        translated = translator.translate(text, src='de', dest='en').text
        language = "en_Translated"
    else:
        translated = text  # If the language is neither English nor German, return the original text
    
    return translated, language

if __name__ == "__main__":
    filename = "Output/voice/" + input("Enter the name for the WAV file (without extension): ") + ".wav"
    print("Press spacebar to start recording...")
    keyboard.wait('space')
    record_audio(filename, duration=5)
    transcription, transcript_filename = transcribe_audio(filename)
    print(f"Transcribed Text for {filename}: {transcription}")
    
    # Translate the transcription
    translated_text, language = detect_and_translate(transcription)
    translated_filename = transcript_filename.replace("text/", "translated_text/").replace(".txt", f"_{language}.txt")
    
    
    with open(translated_filename, "w", encoding="utf-8") as file:
        file.write(translated_text)
    
    print(f"Translated text saved as {translated_filename}")