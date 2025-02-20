from langdetect import detect
from googletrans import Translator

def detect_and_translate(text):
    translator = Translator()
    detected_language = detect(text)
    
    if detected_language == 'en':
        translated = translator.translate(text, src='en', dest='de').text
    elif detected_language == 'de':
        translated = translator.translate(text, src='de', dest='en').text
    else:
        translated = text  # If the language is neither English nor German, return the original text
    
    return translated

if __name__ == "__main__":
    for i in range(1):
        input_file = f"tests/test_outputs/transcription.txt"
        output_file = f"tests/test_outputs/Translated_sample{i}.txt"
        
        with open(input_file, "r", encoding="utf-8") as file:
            transcription = file.read().strip()
        
        translated_text = detect_and_translate(transcription)
        
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(translated_text)
        
        print(f"Translated text for sample{i} saved to {output_file}")