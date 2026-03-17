import os
from typing import Any, Dict, List

import httpx


QALAM_SERVICE_BASE_URL = os.getenv("QALAM_SERVICE_BASE_URL", "http://127.0.0.1:9000")


async def call_qalam_chat(
    session_id: int | None,
    messages: List[Dict[str, str]],
    mode: str,
    metadata: Dict[str, Any] | None = None,
) -> str:
    """
    Call the FastAPI Qalam service /internal/qalam/chat endpoint.
    """
    payload: Dict[str, Any] = {
        "session_id": str(session_id) if session_id is not None else None,
        "messages": messages,
        "mode": mode,
        "metadata": metadata or {},
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"{QALAM_SERVICE_BASE_URL}/internal/qalam/chat", json=payload
        )
        response.raise_for_status()
        data = response.json()
        return data.get("reply", "")


async def call_qalam_translate(
    job_id: int | None,
    text: str,
    source_language: str,
    target_language: str,
    metadata: Dict[str, Any] | None = None,
) -> str:
    """
    Call the FastAPI Qalam service /internal/qalam/translate endpoint.
    """
    payload: Dict[str, Any] = {
        "job_id": str(job_id) if job_id is not None else None,
        "text": text,
        "source_language": source_language,
        "target_language": target_language,
        "metadata": metadata or {},
    }
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            f"{QALAM_SERVICE_BASE_URL}/internal/qalam/translate", json=payload
        )
        response.raise_for_status()
        data = response.json()
        return data.get("translated_text", "")

