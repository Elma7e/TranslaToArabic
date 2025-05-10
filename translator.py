# translator.py

from functools import lru_cache
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

@lru_cache(maxsize=1)
def _get_translator():
    # 1. Load the SentencePiece tokenizer (non-fast) for opus-mt-en-ar
    tokenizer = AutoTokenizer.from_pretrained(
        "Helsinki-NLP/opus-mt-en-ar",
        use_fast=False
    )
    # 2. Load the corresponding seq2seq model
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
    # 3. Build the pipeline
    return pipeline(
        "translation_en_to_ar",
        model=model,
        tokenizer=tokenizer
    )

def translate_en_to_ar(text: str) -> str:
    """
    Translate English `text` to Arabic.
    """
    translator = _get_translator()
    result = translator(text, max_length=512)
    return result[0]['translation_text']
