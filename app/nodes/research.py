from app.workflow.node import Node
from loguru import logger


class ResearchNode(Node):


    name="research"



    def __init__(
        self,
        agent
    ):

        self.agent=agent



    async def run(
        self,
        state
    ):

        result=await self.agent.run(

            task=state.query

        )


        state.research=result


        return state