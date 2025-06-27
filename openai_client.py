import os
from openai import OpenAI
from dotenv import load_dotenv
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()


class OpenAIClient:
    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.7, max_tokens: int = 50):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def _call_api(self, messages: list[ChatCompletionMessageParam]):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response

    def get_message_content(self, messages: list[ChatCompletionMessageParam]) -> str:
        response = self._call_api(messages)
        return response.choices[0].message.content or ""
