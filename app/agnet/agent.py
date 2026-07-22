from app.llm.client import LLMClient

class Agent:
    def __init__(self):
        self.llm = LLMClient()

    async def run(self,message:str):
        messages = [

            {
                "role": "system",
                "content":
                    "你是一个AI助手"
            },

            {
                "role": "user",
                "content": message
            }

        ]
        results = await self.llm.chat(messages)

        return results
