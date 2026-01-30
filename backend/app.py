from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from rag import get_rag_response
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/voice-chat")
async def voice_chat(file: UploadFile):
    audio_bytes = await file.read()

    user_text = speech_to_text(audio_bytes)
    response_text = get_rag_response(user_text)
    audio_response = text_to_speech(response_text)

    return {
        "user_text": user_text,
        "response_text": response_text,
        "audio": audio_response
    }
