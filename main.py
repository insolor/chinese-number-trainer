import random
from tts import create_audio

import streamlit as st
import cn2an


def run_quiz() -> None:
    number = random.randint(0, 99)
    converted = None
    try:
        converted = cn2an.an2cn(number, "low")
    except ValueError:
        st.error(f"Invalid number: {number}")

    if converted:
        st.markdown(converted)
        file = create_audio(converted)
        st.audio(file, format="audio/mpeg", autoplay=True)
        file.unlink()


st.header("Chinese Number Trainer")

start_button = st.button(label="Start")
if start_button:
    run_quiz()
