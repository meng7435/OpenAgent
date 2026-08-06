
from app.agents.base import BaseAgent


class AnalysisAgent(BaseAgent):
    name = 'analysis'

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
                        你是分析专家，
                        负责分析和整理信息。
                        """
                },

                {
                    "role": "user",

                    "content": task

                }

            ]

        )
        return response.content
