from transformers import pipeline

# Only English→Arabic translation
translator = pipeline(
    'translation_en_to_ar',
    model='Helsinki-NLP/opus-mt-en-ar'
)

def translate_en_to_ar(text: str) -> str:
    """
    Translate English `text` to Arabic.
    """
    result = translator(text, max_length=512)
    return result[0]['translation_text']