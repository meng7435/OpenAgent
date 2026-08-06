from app.workflow.node import Node



class WriterNode(Node):


    name="writer"



    def __init__(
        self,
        agent
    ):

        self.agent=agent



    async def run(
        self,
        state
    ):


        task=f"""

生成最终报告。


资料:

{state.research}


分析:

{state.analysis}

"""


        result=await self.agent.run(

            task

        )


        state.report=result


        return state