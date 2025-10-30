import streamlit as st
from googletrans import Translator
from gtts import gTTS
import base64

# Page Setup
st.set_page_config(page_title="🌍 Language Translator", page_icon="🌐", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌍 Language Translation App</h1>", unsafe_allow_html=True)

translator = Translator()

# Input Box
input_text = st.text_area("✍ Enter text to translate:", height=150)

# Language List
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Marathi": "mr",
    "Japanese": "ja"
}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("🌐 Source Language:", list(languages.keys()))
with col2:
    target_lang = st.selectbox("🌐 Target Language:", list(languages.keys()))

# Translate Button
if st.button("🔁 Translate Now"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter text!")
    else:
        result = translator.translate(input_text, src=languages[source_lang], dest=languages[target_lang])
        translated_text = result.text

        st.success("✅ Translation Successful!")
        output_box = st.text_area("🎯 Translated Output:", translated_text, height=150)

        # ✅ Copy Button
        st.code(f"{translated_text}")
        st.write("📋 Copy the highlighted text above")

        # ✅ Text to Speech Button
        if st.button("🔊 Listen to Translation"):
            tts = gTTS(translated_text, lang=languages[target_lang])
            audio_file = "audio.mp3"
            tts.save(audio_file)

            with open(audio_file, "rb") as audio:
                audio_bytes = audio.read()
                st.audio(audio_bytes, format="audio/mp3")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>💡 Developed using Python & Streamlit</p>", unsafe_allow_html=True)
