from app.agents.base import BaseAgent


class WriterAgent(
    BaseAgent
):
    name = "writer"

    description = """
    负责生成最终报告
    """

    async def run(
            self,
            task
    ):
        response = await self.llm.chat(

            [

                {
                    "role": "system",

                    "content":
                        """
                        你是写作专家。
                        """
                },

                {
                    "role": "user",

                    "content": task

                }

            ]

        )

        return response.content
