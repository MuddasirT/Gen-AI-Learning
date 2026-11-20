"""
Day 01: Minimal Python client for a local Ollama chat model.

Prerequisites:
    1. Install and start Ollama.
    2. Download the model: ollama pull qwen3:14b
    3. Run: python app.py

This example uses only Python's standard library.
"""

import json
import urllib.error
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:14b"


def ask_ollama(question: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are Andy, a clear and helpful AI learning assistant.",
            },
            {"role": "user", "content": question},
        ],
        "stream": False,
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["message"]["content"]
    except urllib.error.URLError as error:
        raise RuntimeError(
            "Could not reach Ollama. Check that Ollama is running "
            "and that the model is available."
        ) from error
    except (KeyError, json.JSONDecodeError) as error:
        raise RuntimeError("Ollama returned an unexpected response.") from error


if __name__ == "__main__":
    print(f"Andy is using {MODEL}. Type 'exit' to quit.\n")

    while True:
        user_question = input("You: ").strip()
        if user_question.lower() in {"exit", "quit"}:
            print("Andy: See you next time!")
            break
        if not user_question:
            continue

        try:
            print("\nAndy:", ask_ollama(user_question), "\n")
        except RuntimeError as error:
            print(f"Error: {error}\n")
