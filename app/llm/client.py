from openai import AsyncOpenAI
from app.config import settings

class LLMClient:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_API_URL,
        )
    async def chat(self,messages,tools=None):
        response = await self.client.chat.completions.create(

            model=settings.MODEL,

            messages=messages,

            temperature=0,

            tools=tools,

            tool_choice="auto"
        )
        return response.choices[0].message

