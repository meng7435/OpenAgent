from app.workflow.node import Node



class AnalysisNode(Node):


    name="analysis"



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

根据资料分析:

{state.research}

"""


        result=await self.agent.run(

            task

        )


        state.analysis=result


        return state