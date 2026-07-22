from openai import AsyncOpenAI
from app.config.seetings import settings

class LLMClient:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_API_URL,
        )
    async def chat(self,messages):
        response = await self.client.chat.completions.create(

            model=settings.MODEL,

            messages=messages,

            temperature=0

        )
        return response.choices[0].message.content

