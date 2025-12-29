import requests
from .config import OLLAMA_URL, MODEL_NAME

def generate_summary(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response generated.")
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama: {str(e)}"
