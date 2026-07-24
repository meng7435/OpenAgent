from app.llm.client import LLMClient
from app.tools import create_tool_manager
import json
from app.memory.manager import MemoryManager


class Agent:
    def __init__(self):
        self.llm = LLMClient()
        self.tool_manager = create_tool_manager()
        self.memory = MemoryManager()

    async def run(self, message, session_id):
        history = await self.memory.get_history(session_id)
        messages = [
            {
                "role": "system",
                "content":
                    "你是一个AI Agent"
            }
        ]
        messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": message
            }
        )
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
                    result = await self.tool_manager.execute(

                        tool_name,

                        arguments

                    )
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
                final_answer = response.content

                await self.memory.save_message(

                    session_id,

                    {
                        "role": "user",

                        "content": message
                    }

                )

                await self.memory.save_message(

                    session_id,

                    {
                        "role": "assistant",

                        "content": final_answer
                    }

                )

                return final_answer
