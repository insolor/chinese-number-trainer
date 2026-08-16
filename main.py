import random
from tts import create_audio

import streamlit as st
import cn2an


def convert_number_to_cn(number: int) -> str:
    return cn2an.an2cn(number, "low")


def run_quiz(top: int) -> None:
    number = random.randint(0, top)
    converted = None
    try:
        converted = convert_number_to_cn(number)
    except ValueError:
        st.error(f"Invalid number: {number}")

    if converted:
        st.markdown(converted)  # TODO: don't show converted, add quiz
        file = create_audio(converted)
        try:
            st.audio(file, format="audio/mpeg", autoplay=True)
        finally:
            file.unlink()


st.header("Chinese Number Trainer")

top = st.radio("Top number", options=[10, 100, 1000, 10_000, 100_000])

start_button = st.button(label="Start")
if start_button:
    run_quiz(top)
