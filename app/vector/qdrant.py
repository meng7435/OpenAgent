from qdrant_client import QdrantClient

from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)


class QdrantStore:

    def __init__(self):
        self.client = QdrantClient(
            ":memory:"
        )

        self.collection = "memory"

    # 创建向量数据库
    async def create_collection(
            self,
            dim
    ):
        self.client.create_collection(

            collection_name=self.collection,

            vectors_config=
            VectorParams(

                size=dim,

                distance=Distance.COSINE

            )

        )

    # 存入数据
    async def add(
            self,
            id,
            vector,
            payload
    ):
        self.client.upsert(

            collection_name=self.collection,

            points=[

                PointStruct(

                    id=id,

                    vector=vector,

                    payload=payload

                )

            ]

        )

    # 查询
    async def search(
            self,
            vector,
            limit=10
    ):
        result = self.client.query_points(
            collection_name=self.collection,
            query=vector,
            limit=limit,
            with_payload=True,  # 控制是否返回业务数据
            with_vectors=False
        )
        return result
