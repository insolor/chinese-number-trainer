from gtts import gTTS
from pathlib import Path
from uuid import uuid4

language = "zh"
audio_directory = Path("audio")
audio_directory.mkdir(parents=True, exist_ok=True)


def create_audio(text: str) -> Path:
    file = audio_directory / f"{uuid4()}.mp3"
    tts = gTTS(text, lang=language)
    tts.save(file)
    return file
