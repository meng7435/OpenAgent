from abc import ABC, abstractmethod


class BaseMemory(ABC):
    @abstractmethod
    async def add(self, key, value):
        pass

    @abstractmethod
    async def get(self, key):
        pass

    @abstractmethod
    async def clear(self,key):
        pass