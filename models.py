import os
from abc import ABC, abstractmethod
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AIModel(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

class GroqModel(AIModel):
    def __init__(self, model_name: str):
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("GROQ_API_KEY")
        )
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

class ModelFactory:
    _models = {
        0: {"name": "llama-3.3-70b-versatile", "class": GroqModel},
        1: {"name": "llama-3.1-8b-instant",     "class": GroqModel},
        2: {"name": "qwen/qwen3-32b",            "class": GroqModel},
    }

    @classmethod
    def get_model(cls, model_key: int) -> AIModel:
        if model_key not in cls._models:
            raise ValueError(f"Geçersiz model: {model_key}")
        info = cls._models[model_key]
        return info["class"](model_name=info["name"])