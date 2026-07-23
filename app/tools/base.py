from abc import ABC, abstractmethod


class BaseTool(ABC):
    name = ''

    description: str = ''

    @abstractmethod
    async def execute(self, **kwargs):
        pass


    def schema(self):
        return {

            "type": "function",

            "function": {

                "name": self.name,

                "description":
                    self.description,

                "parameters": {

                    "type": "object",

                    "properties": {}

                }

            }

        }