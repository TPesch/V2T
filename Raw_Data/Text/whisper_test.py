import whisper
import os

def transcribe_audio(audio_path, output_txt):
    print(f"Loading Whisper model for {audio_path}...")
    model = whisper.load_model("base")

    print(f"Transcribing audio {audio_path}...")
    result = model.transcribe(audio_path)

    transcription = result["text"]
    print(f"Transcription for {audio_path}:", transcription)

    with open(output_txt, "w", encoding="utf-8") as file:
        file.write(transcription)

    print(f"Transcription saved to {output_txt}")

if __name__ == "__main__":
    for i in range(1, 21):
        audio_file = f"Raw_Data/voices/sample{i}.wav"
        output_file = f"Raw_Data/Text/Predicted/transcription_sample{i}.txt"
        transcribe_audio(audio_file, output_file)
