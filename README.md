# Local AI Prompt Sender

A desktop application to send prompts to multiple LLM models via the Groq API.

## Requirements

- Python 3.9+
- Groq API key → [console.groq.com](https://console.groq.com)

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
   cd REPO_NAME
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

4. Open `.env` and enter your Groq API key:
   ```
   GROQ_API_KEY=gsk_...
   ```

5. Run the app:
   ```bash
   python main.py
   ```

## Available Models

| Option | Model |
|--------|-------|
| Llama 3.3 70B | llama-3.3-70b-versatile |
| Llama 3.1 8B | llama-3.1-8b-instant |
| Qwen3 32B | qwen/qwen3-32b |
