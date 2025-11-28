import streamlit as st
from gtts import gTTS
from pathlib import Path

st.header("Chinese Number Trainer")

filename = Path("audio/audio.mp3")
filename.parent.mkdir(parents=True, exist_ok=True)

text = st.text_input(label="Text")
button = st.button("Generate")

language = "zh"

if button:
    tts = gTTS(text, lang=language)
    tts.save(filename)
    st.audio(filename, format="audio/mpeg", autoplay=True)
