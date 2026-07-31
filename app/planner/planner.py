import json

from app.planner.schema import Plan


class Planner:

    def __init__(
            self,
            llm
    ):
        self.llm = llm

    async def create_plan(
            self,
            message,
            skills
    ):
        prompt = f"""

你是任务规划器。


用户任务:

{message}


可用技能:

{skills}


请拆分任务。


返回JSON:

{{
"tasks":[

{{
"skill":"",
"input":{{}}
}}

]

}}

"""

        response = await self.llm.chat(

            [
                {
                    "role": "system",
                    "content": prompt
                }
            ]

        )

        data = json.loads(
            response.content
        )

        return Plan(
            **data
        )
