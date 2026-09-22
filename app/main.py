from fastapi import FastAPI
import os

def create_app() -> FastAPI:
    app = FastAPI(
        title="Enterprise RAG Chatbot API",
        description="Backend chatbot terskala dengan arsitektur modular.",
        version="1.0.0"
    )
    app.include_router(chat_router, prefix="/api/v1", tags=["Chat"])

    return app

app = create_app()