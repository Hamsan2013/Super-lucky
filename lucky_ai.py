import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = (
    "You are Lucky — a friendly helpful AI. "
    "Always stay positive and safe."
)

class LuckyAI:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def chat(self, user_msg):
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ]
        )
        return resp["choices"][0]["message"]["content"]
