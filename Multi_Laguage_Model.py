from transformers import pipeline

def translate_sentence(sentence, target_languages):
    # Load the translation pipeline
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-multilingual")

    translations = {}
    for language in target_languages:
        # Translate the sentence to the target language
        translation = translator(sentence, src="en", tgt=language)
        translations[language] = translation[0]['translation_text']

    return translations



def get_sentence(a):
    sentence = a

# Target languages
    target_languages = ["fr", "es", "de"]  # French, Spanish, German

# Translate the sentence into multiple languages
    translations = translate_sentence(sentence, target_languages)

# Print translations
for lang, translation in translations.items():
    print(f"{lang}: {translation}")
