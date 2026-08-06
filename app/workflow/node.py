from abc import ABC,abstractmethod



class Node(ABC):


    name:str



    @abstractmethod
    async def run(
        self,
        state
    ):

        pass