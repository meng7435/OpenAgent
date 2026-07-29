from abc import ABC, abstractmethod

class Skill(ABC):
    name = ''

    description = ''

    @abstractmethod
    async def execute(self,input):
        pass