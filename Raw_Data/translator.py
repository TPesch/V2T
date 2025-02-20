from langdetect import detect
from googletrans import Translator

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
    for i in range(1, 21):
        input_file = f"Raw_Data/Text/Original/reference{i}.txt"
        
        with open(input_file, "r", encoding="utf-8") as file:
            transcription = file.read().strip()
        
        translated_text, language = detect_and_translate(transcription)
        output_file = f"Raw_Data/Text/Translated/Translated_sample_{language}_{i}.txt"
        
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(translated_text)
        
        print(f"Translated text for sample{i} saved to {output_file}")