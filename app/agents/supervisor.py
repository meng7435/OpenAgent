import json



class SupervisorAgent:


    def __init__(
        self,
        llm,
        manager
    ):

        self.llm=llm

        self.manager=manager



    async def plan(
        self,
        task
    ):


        agents=self.manager.descriptions()


        prompt=f"""

你是任务管理者。


任务:

{task}


可用Agent:

{agents}


选择执行者。


返回JSON:

{{
"agent":"",
"task":""
}}

"""

        response = await self.llm.chat(
            messages=[
                {
                    "role": "system",
                    "content": prompt
                }
            ]
        )


        return json.loads(
            response.content
        )