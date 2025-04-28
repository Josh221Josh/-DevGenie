import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = "https://api.openai.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def call_openai(prompt: str, role: str = "user") -> str:
    payload = {
        "model": "gpt-4",
        "messages": [{"role": role, "content": prompt}],
    }
    response = httpx.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def generate_code(prompt: str) -> str:
    return call_openai(f"Write code for the following request: {prompt}")


def explain_code(code: str) -> str:
    return call_openai(f"Explain what this code does: {code}")


def debug_code(error: str) -> str:
    return call_openai(f"Debug this error: {error}")


def optimize_code(code: str) -> str:
    return call_openai(f"Optimize this code for performance: {code}")
