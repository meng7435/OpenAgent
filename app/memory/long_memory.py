from app.memory.base import BaseMemory

from app.vector.qdrant import QdrantStore

from app.embedding.encoder import Embedding

import uuid


class LongMemory:
    # 静态变量：保存全局唯一实例，挂载在类本身，不属于对象
    _instance = None

    # __new__：负责创建对象实例（分配内存），在 __init__ 之前执行
    def __new__(cls):
        # 判断是否还没有创建实例
        if cls._instance is None:
            # 创建唯一实例，存入类变量
            cls._instance = super().__new__(cls)
        # 无论新建还是已有，永远返回同一个实例
        return cls._instance

    # __init__：对象创建完成后，初始化属性（给对象赋值）
    def __init__(self):
        # 关键判断：如果对象已经初始化过，直接return，不再重复执行
        if hasattr(self, "initialized"):
            return
        self.vector = QdrantStore()
        self.embedding = Embedding()
        self.initialized = False

    async def init(self):
        if not self.initialized:
            vector = self.embedding.encode(
                "test"
            )

            await self.vector.create_collection(
                len(vector)
            )

            self.initialized = True

    async def add(
            self,
            user_id,
            text: str
    ):
        await self.init()

        vector = self.embedding.encode(
            text
        )

        await self.vector.add(

            str(uuid.uuid4()),

            vector,

            {
                "user_id": user_id,

                "content": text
            }

        )

    async def search(
            self,
            query
    ):
        await self.init()

        vector = self.embedding.encode(
            query
        )

        result = await self.vector.search(
            vector
        )

        return result
