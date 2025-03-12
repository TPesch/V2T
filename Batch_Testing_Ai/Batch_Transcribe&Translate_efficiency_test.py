import os
import whisper
from langdetect import detect
from googletrans import Translator

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

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



def transcribleFunction(transcribe_audio, detect_and_translate, input_folder, output_folder):
    for i in range(1, 17):
        input_file = os.path.join(input_folder, f"sample{i}.wav")
        
        if not os.path.exists(input_file):
            print(f"File not found: {input_file}")
            continue
        
        transcription = transcribe_audio(input_file)
        
        if transcription:
            translated_text, language = detect_and_translate(transcription)
            output_file = os.path.join(output_folder, f"Translated_sample_{language}_{i}.txt")
            
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(f"Original: \"{transcription}\" --> {language.split('_')[0]} translation: \"{translated_text}\"")
            
            print(f"Translated text for sample{i} saved to {output_file}")
        else:
            print(f"Could not transcribe audio file: {input_file}")

if __name__ == "__main__":
    input_folder = "Batch_Testing_Ai/Voices/English"
    output_folder = "Batch_Testing_Ai/Voices/English/Translated"
    os.makedirs(output_folder, exist_ok=True)
    
    transcribleFunction(transcribe_audio, detect_and_translate, input_folder, output_folder)
    
    input_folder = "Batch_Testing_Ai/Voices/German"
    output_folder = "Batch_Testing_Ai/Voices/German/Translated"
    transcribleFunction(transcribe_audio, detect_and_translate, input_folder, output_folder)

