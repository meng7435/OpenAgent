from app.memory.short_memory import ShortMemory

from app.memory.long_memory import LongMemory


class MemoryManager:
    def __init__(self):
        self.short = ShortMemory()
        self.long = LongMemory()

    async def save_message(self, session_id, message
                           ):
        await self.short.add(

            session_id,

            message

        )

    async def get_history(self, session_id):
        return await self.short.get(
            session_id
        )

    async def save_user_memory(self, user_id, info:str):
        await self.long.add(

            user_id,

            info

        )

    async def get_user_memory(self, user_id):
        return await self.long.get(
            user_id
        )

    async def recall_memory(
            self,
            query
    ):
        return await self.long.search(
            query
        )