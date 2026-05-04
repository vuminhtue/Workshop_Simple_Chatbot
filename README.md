# Chatbot (Ollama backend + Gradio frontend)

This small app runs a Gradio-based chat UI that uses an Ollama model (default: `gemma3:12b`) as the LLM.

Prerequisites
- Ollama running locally (https://ollama.ai) OR the `ollama` CLI available in PATH.
- Python 3.9+ and pip

Install

1. Create a virtual environment and activate it.

```
conda create -n mychat python=3.10 pip
conda activate mychat
```

2. Install dependencies:

```
pip install -r requirements.txt
```

Environment
- `OLLAMA_API_URL` — optional; defaults to `http://localhost:11434`
- `OLLAMA_MODEL` — optional; defaults to `gemma3:1b`

Run gradio model

```
python app.py
```

Open the Gradio UI at http://localhost:7860 in your browser.
