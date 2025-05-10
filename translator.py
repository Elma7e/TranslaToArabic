from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def _get_translator():
    # initialize once
    return pipeline(
        'translation_en_to_ar',
        model='Helsinki-NLP/opus-mt-en-ar'
    )

def translate_en_to_ar(text: str) -> str:
    """
    Translate English `text` to Arabic.
    """
    translator = _get_translator()
    result = translator(text, max_length=512)
    return result[0]['translation_text']
