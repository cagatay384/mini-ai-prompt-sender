# Local AI Prompt Sender

Groq API üzerinden birden fazla LLM modeline prompt gönderebileceğin masaüstü uygulaması.

## Gereksinimler

- Python 3.9+
- Groq API key → [console.groq.com](https://console.groq.com)

## Kurulum

1. Repoyu klonla:
   ```bash
   git clone https://github.com/KULLANICI_ADIN/REPO_ADIN.git
   cd REPO_ADIN
   ```

2. Bağımlılıkları yükle:
   ```bash
   pip install -r requirements.txt
   ```

3. `.env.example` dosyasını `.env` olarak kopyala:
   ```bash
   cp .env.example .env
   ```

4. `.env` dosyasını aç ve kendi Groq API key'ini gir:
   ```
   GROQ_API_KEY=gsk_...
   ```

5. Uygulamayı çalıştır:
   ```bash
   python main.py
   ```

## Modeller

| Seçenek | Model |
|---------|-------|
| Llama 3.3 70B | llama-3.3-70b-versatile |
| Llama 3.1 8B | llama-3.1-8b-instant |
| Qwen3 32B | qwen/qwen3-32b |
