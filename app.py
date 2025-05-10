import streamlit as st
from translator import translate_en_to_ar
from grammar import correct_grammar

st.set_page_config(page_title="English→Arabic Translator & Grammar Checker")

st.title("🇬🇧→🇸🇦 English→Arabic & Grammar Correction")

# Input area
text = st.text_area("Enter English text:")

# Buttons for features
col1, col2 = st.columns(2)
with col1:
    if st.button("Translate to Arabic"):
        with st.spinner("Translating..."):
            try:
                arabic = translate_en_to_ar(text)
                st.success(arabic)
            except Exception as e:
                st.error(f"Translation error: {e}")

with col2:
    if st.button("Check Grammar"):
        with st.spinner("Correcting..."):
            try:
                corrected = correct_grammar(text)
                st.success(corrected)
            except Exception as e:
                st.error(f"Grammar correction error: {e}")