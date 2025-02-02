import whisper

def transcribe_audio(audio_path, output_txt="tests/test_outputs/transcription.txt"):
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing audio...")
    result = model.transcribe(audio_path)

    transcription = result["text"]
    print("Transcription:", transcription)

    with open(output_txt, "w", encoding="utf-8") as file:
        file.write(transcription)

    print(f"Transcription saved to {output_txt}")

if __name__ == "__main__":
    audio_file = "tests/test_outputs/test_audio.wav"  
    transcribe_audio(audio_file)

