from gtts import gTTS
import base64
import tempfile

def text_to_speech(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        audio_bytes = open(f.name, "rb").read()
    return base64.b64encode(audio_bytes).decode()
