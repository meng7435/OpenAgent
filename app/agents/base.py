from abc import ABC, abstractmethod
class BaseAgent(ABC):

    name:str

    description:str

    def __init__(self,llm):
        self.llm = llm

    @abstractmethod
    async def run(self,task):
        pass
