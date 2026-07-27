from sentence_transformers import SentenceTransformer


class Embedding:
    def __init__(self):
        self.model = SentenceTransformer("bge-small-zh-v1.5")

    def encode(self, text):
        vector = self.model.encode(
            text
        )

        return vector.tolist()
