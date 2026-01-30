# Real-Time Voice AI Agent with RAG

This project implements a real-time voice-enabled AI assistant using
Speech-to-Text, Retrieval-Augmented Generation (RAG), and Text-to-Speech.

## Features
- Real-time voice input and response
- RAG-based intelligent answers
- FastAPI backend
- React frontend
- Low-latency processing

## Tech Stack
- FastAPI
- React + TypeScript
- OpenAI / Whisper
- LangChain + ChromaDB
- gTTS

## Run Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
