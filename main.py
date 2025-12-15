from uuid import uuid4
import streamlit as st
from gtts import gTTS
from pathlib import Path

st.header("Chinese Number Trainer")

audio_directory = Path("audio")
audio_directory.mkdir(parents=True, exist_ok=True)

text = st.text_input(label="Text")
button = st.button("Generate", disabled=not text)

language = "zh"

if button:
    file = audio_directory / f"{uuid4()}.mp3"
    tts = gTTS(text, lang=language)
    tts.save(file)
    st.audio(file, format="audio/mpeg", autoplay=True)
    file.unlink()
