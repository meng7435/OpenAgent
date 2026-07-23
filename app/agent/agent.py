from app.llm.client import LLMClient
from app.tools import create_tool_manager
import json

class Agent:
    def __init__(self):
        self.llm = LLMClient()
        self.tool_manager = create_tool_manager()

    async def run(
            self,
            message
    ):

        messages = [

            {
                "role": "system",

                "content":
                    "你是一个AI Agent"
            },

            {
                "role": "user",

                "content": message
            }

        ]

        while True:

            response = await self.llm.chat(

                messages,

                self.tool_manager.get_schemas()

            )

            # 判断是否调用工具

            if response.tool_calls:

                for call in response.tool_calls:
                    tool_name = call.function.name

                    arguments = json.loads(

                        call.function.arguments

                    )
                    print(tool_name)
                    print(arguments)
                    result = await self.tool_manager.execute(

                        tool_name,

                        arguments

                    )
                    print(result)
                    messages.append(

                        response

                    )

                    messages.append(

                        {

                            "role": "tool",

                            "tool_call_id":
                                call.id,

                            "content":
                                str(result)

                        }

                    )



            else:

                return response.content