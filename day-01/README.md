# Day 01: First Local LLM Application

**Learner:** Muddasir  
**Status:** Core practical milestone completed

## Objective

Understand the basic role of an LLM, run a local model with Ollama, and call it from a Python application over HTTP.

## Environment used

- macOS, Apple M4, 24 GB unified memory
- Python 3.13.9
- Ollama
- Model: `qwen3:14b`
- Ollama API: `http://localhost:11434/api/chat`

## What was completed

1. Checked the local development environment and available Ollama models.
2. Ran Qwen3 locally through Ollama.
3. Explored how a transformer-based LLM predicts the next token.
4. Built a Python application that sends chat messages to Ollama using an HTTP POST request with JSON.
5. Received and displayed a model response in Python.
6. Discussed the difference between an LLM and an AI agent.

## Architecture

```text
Python app (app.py)
      |
      | HTTP POST + JSON
      v
Ollama API (localhost:11434)
      |
      v
Qwen3 14B local model
      |
      v
JSON response
      |
      v
Python prints assistant response
```

## Run it

Make sure Ollama is running and the model is available:

```bash
ollama list
ollama run qwen3:14b
```

In a separate terminal:

```bash
cd day-01
python3 -m venv .venv
source .venv/bin/activate
python app.py
```

The sample application is in [app.py](./app.py).

## Concepts to remember

- **LLM:** A model that processes input tokens and generates output tokens.
- **Ollama:** Runs local models and exposes an HTTP API.
- **Python client:** Our application; it sends requests and handles responses.
- **HTTP:** The communication protocol between our Python process and Ollama.
- **JSON:** The structured data format used for the request and response.
- **Conversation history:** The application must send relevant prior messages on later requests. A stateless API call does not automatically remember earlier calls.

## Important architecture notes

- The model generates output token by token.
- Modern decoder-only transformers commonly use causal self-attention.
- Positional information may use methods such as RoPE; it is not always a simple position vector added to embeddings.
- During inference, a KV cache can reuse prior attention keys and values.
- The exact architecture details vary by model family and version.

## Remaining Day 01 sign-off

- [ ] Explain the Python HTTP request and JSON response line by line.
- [ ] Pass the three-question knowledge check.
- [ ] Confirm the local application runs independently.

## Next

**Day 02: Conversation Memory and Context Management**

We will maintain a message history in Python and send the conversation context with each request.
