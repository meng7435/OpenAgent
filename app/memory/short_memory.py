from app.memory.base import BaseMemory


class ShortMemory(BaseMemory):
    def __init__(self):
        self.storage = {}

    async def add(self, key, value):
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append(
            value
        )

    async def get(self, key):
        return self.storage.get(
            key,
            []
        )

    async def clear(self, key):
        if key in self.storage:
            del self.storage[key]
