from tts import create_audio

import streamlit as st
import cn2an

st.header("Chinese Number Trainer")

text = st.text_input(label="Enter a number")
if text:
    converted = None
    try:
        converted = cn2an.an2cn(text, "low")
    except ValueError:
        md = st.error("Invalid input")

    if converted:
        md = st.markdown(converted)
        file = create_audio(converted)
        st.audio(file, format="audio/mpeg", autoplay=True)
        file.unlink()
