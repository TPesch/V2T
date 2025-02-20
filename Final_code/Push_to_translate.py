import os
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import keyboard
from langdetect import detect, LangDetectException
from googletrans import Translator

def record_audio(filename, fs=16000):
    print(f"Recording {filename}...")
    recording = []
    def callback(indata, frames, time, status):
        recording.append(indata.copy())
    
    with sd.InputStream(samplerate=fs, channels=1, callback=callback, dtype='int16'):
        print("Press 's' to stop recording...")
        keyboard.wait('s', suppress=True)
        print("Recording stopped...")
    
    recording = np.concatenate(recording, axis=0)
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
    
    return transcription

def detect_and_translate(text):
    translator = Translator()
    try:
        detected_language = detect(text)
    except LangDetectException:
        detected_language = "unknown"
    
    if detected_language == 'en':
        translated = translator.translate(text, src='en', dest='de').text
        label = "EN->DE"
    elif detected_language == 'de':
        translated = translator.translate(text, src='de', dest='en').text
        label = "DE->EN"
    else:
        translated = text  # If the language is neither English nor German, return the original text
        label = "NA"
    
    return translated, label

if __name__ == "__main__":
    session_name = input("Enter the session name: ")
    os.makedirs(f"Final_code/Live_Transcriptions/{session_name}", exist_ok=True)
    
    transcript_file = f"Final_code/Live_Transcriptions/{session_name}/{session_name}_transcript.txt"
    translated_file = f"Final_code/Live_Transcriptions/{session_name}/{session_name}_translated.txt"
    
    session_count = 1
    
    while True:
        print("Press spacebar to start recording (press 's' to stop, 'q' to quit)...")
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN and key.name == 'space':
            filename = f"Final_code/Live_Transcriptions/{session_name}/session{session_count}.wav"
            record_audio(filename)
            transcription = transcribe_audio(filename)
            print(f"Transcribed Text: {transcription}")
            
            # Save transcription to the session transcript file
            with open(transcript_file, "a", encoding="utf-8") as file:
                file.write(f"Session {session_count}:\n{transcription}\n\n")
            
            # Translate the transcription
            translated_text, label = detect_and_translate(transcription)
            print(f"Translated Text: {translated_text}")
            
            # Save translated text to the session translated file
            with open(translated_file, "a", encoding="utf-8") as file:
                file.write(f"Session {session_count} ({label}):\n{translated_text}\n\n")
            
            print(f"Translated text saved as {translated_file}")
            session_count += 1
        elif key.event_type == keyboard.KEY_DOWN and key.name == 'q':
            break