from transformers import pipeline

# T5-based grammar correction
grammar_pipeline = pipeline(
    'text2text-generation',
    model='vennify/t5-base-grammar-correction',
    tokenizer='vennify/t5-base-grammar-correction'
)

def correct_grammar(text: str) -> str:
    """
    Correct grammatical errors in the input English `text`.
    """
    # Prefix as required by the model
    input_text = f"fix grammar: {text.strip()}"
    outputs = grammar_pipeline(input_text, max_length=512)
    return outputs[0]['generated_text']