class MultiAgentSystem:


    def __init__(
        self,
        supervisor,
        manager
    ):

        self.supervisor=supervisor

        self.manager=manager



    async def run(
        self,
        task
    ):


        result=[]


        for i in range(5):


            decision = await self.supervisor.plan(
                task
            )


            if decision["agent"]=="finish":

                break



            agent=self.manager.get(

                decision["agent"]

            )


            output=await agent.run(

                decision["task"]

            )


            result.append(output)



            task=f"""

原任务:

{task}


已有结果:

{result}

继续执行

"""



        return result[-1]