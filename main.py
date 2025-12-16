from uuid import uuid4
import streamlit as st
from gtts import gTTS
from pathlib import Path
import cn2an

language = "zh"

st.header("Chinese Number Trainer")

audio_directory = Path("audio")
audio_directory.mkdir(parents=True, exist_ok=True)

text = st.text_input(label="Enter a number")
if text:
    converted = None
    try:
        converted = cn2an.an2cn(text, "low")
    except ValueError:
        md = st.error("Invalid input")

    if converted:
        md = st.markdown(converted)
        file = audio_directory / f"{uuid4()}.mp3"
        tts = gTTS(converted, lang=language)
        tts.save(file)
        st.audio(file, format="audio/mpeg", autoplay=True)
        file.unlink()
