from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ollama_client import chat as ollama_chat, generate as ollama_generate


app = FastAPI(title="Qalam Service", version="0.1.0")


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    messages: List[ChatMessage]
    mode: str = "chat"
    metadata: Dict[str, Any] | None = None


class ChatResponse(BaseModel):
    reply: str
    used_mode: str


class TranslateRequest(BaseModel):
    job_id: Optional[str] = None
    text: str
    source_language: str
    target_language: str
    metadata: Dict[str, Any] | None = None


class TranslateResponse(BaseModel):
    translated_text: str


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/internal/qalam/chat", response_model=ChatResponse)
async def qalam_chat(request: ChatRequest) -> ChatResponse:
    try:
        # Prepend a system prompt depending on mode
        system_content = "You are a helpful literary assistant."
        if request.mode == "translation":
            system_content = (
                "You are a professional literary translator. Preserve style, tone, "
                "and character voices while translating."
            )
        elif request.mode == "summary":
            system_content = (
                "You summarize chapters of novels in clear Arabic, preserving key events and emotions."
            )

        messages = [{"role": "system", "content": system_content}] + [
            m.model_dump() for m in request.messages
        ]

        reply_text = await ollama_chat(messages)
        return ChatResponse(reply=reply_text, used_mode=request.mode)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/internal/qalam/translate", response_model=TranslateResponse)
async def qalam_translate(request: TranslateRequest) -> TranslateResponse:
    try:
        prompt = (
            f"Translate the following literary text from {request.source_language} "
            f"to {request.target_language}, preserving style and character voice:\n\n"
            f"{request.text}"
        )
        translated = await ollama_generate(prompt)
        return TranslateResponse(translated_text=translated)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc

