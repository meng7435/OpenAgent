from app.memory.base import BaseMemory


class LongMemory(BaseMemory):
    def __init__(self):
        self.storage = []

    async def add(self, key, value):
        self.storage.append(

            {
                "key": key,

                "value": value

            }

        )

    async def get(self, key):
        result = []

        for item in self.storage:

            if item["key"] == key:
                result.append(
                    item["value"]
                )

        return result

    async def clear(self, key):
        self.storage = [

            item

            for item in self.storage

            if item["key"] != key

        ]
