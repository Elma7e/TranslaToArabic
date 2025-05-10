from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def _get_grammar_pipeline():
    # initialize once
    return pipeline(
        'text2text-generation',
        model='vennify/t5-base-grammar-correction',
        tokenizer='vennify/t5-base-grammar-correction'
    )

def correct_grammar(text: str) -> str:
    """
    Correct grammatical errors in the input English `text`.
    """
    pipe = _get_grammar_pipeline()
    input_text = f"fix grammar: {text.strip()}"
    outputs = pipe(input_text, max_length=512)
    return outputs[0]['generated_text']
