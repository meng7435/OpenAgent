from nltk.chat.zen import responses

from app.agents.base import BaseAgent


class ResearchAgent(BaseAgent):
    name = 'research'

    description = """
      负责信息搜索和资料整理
      """

    async def run(self, task):
        response = await self.llm.chat(

            [
                {
                    "role": "system",

                    "content":
                        """
                        你是研究专家，
                        负责收集和整理信息。
                        """
                },

                {
                    "role": "user",

                    "content": task

                }

            ]

        )
        return response.content
