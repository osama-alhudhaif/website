import os
from typing import Any, Dict, List
import httpx

# إعدادات الموديل والروابط (تأكد من استخدام النقطتين :)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3:70b")

async def chat(messages: List[Dict[str, str]], **params: Any) -> str:
    """
    إرسال محادثة إلى Ollama واستلام الرد كاملاً (بدون Stream)
    """
    async with httpx.AsyncClient(timeout=120.0) as client:  # زدنا المهلة لأن 70B ضخم
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json={
                "model": OLLAMA_MODEL_NAME,
                "messages": messages,
                "stream": False,  # ضروري جداً لمنع خطأ الـ Extra data
                **params,
            },
        )
        response.raise_for_status()
        data = response.json()
        # استخراج محتوى الرد من هيكلة Ollama
        return data.get("message", {}).get("content", "")

async def generate(prompt: str, **params: Any) -> str:
    """
    توليد نص مباشر من Ollama واستلام الرد كاملاً
    """
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL_NAME,
                "prompt": prompt,
                "stream": False,  # ضروري جداً لمنع خطأ الـ Extra data
                **params,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")