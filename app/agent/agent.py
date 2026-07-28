import traceback
from logging import setLogRecordFactory

from app.llm.client import LLMClient
from app.mcp.client import MCPClient
from app.mcp import server
from app.tools import create_tool_manager
import json
from app.memory.manager import MemoryManager
from loguru import logger

class Agent:
    def __init__(self):
        self.llm = LLMClient()
        self.mcp = MCPClient(server)
        self.memory = MemoryManager()

    async def run(self, message, session_id):
        # 加载历史记录
        history = await self.memory.get_history(session_id)
        messages = [{"role": "system", "content": "你是一个AI Agent"}]
        valid_history = []
        for item in history:
            if isinstance(item, dict):
                valid_history.append(item)
        messages.extend(valid_history)

        user_input_msg = {"role": "user", "content": message}
        messages.append(user_input_msg)
        tools = await self.mcp.get_tools()
        while True:
            response = await self.llm.chat(messages, tools)
            if response.tool_calls:
                assistant_call_msg = response.model_dump(mode="json")
                messages.append(assistant_call_msg)

                for call in response.tool_calls:
                    tool_name = call.function.name
                    city = json.loads(call.function.arguments)['city']
                    result = await self.mcp.tool_run(tool_name, city)
                    tool_msg = {
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": str(result)
                    }
                    messages.append(tool_msg)

                continue

            else:
                final_answer = response.content
                assistant_final_msg = {"role": "assistant", "content": final_answer}

                try:
                    await self.memory.save_message(session_id, user_input_msg)
                    await self.memory.save_message(session_id, assistant_final_msg)

                    await self.memory.save_user_memory(session_id, message)
                    await self.memory.save_user_memory(session_id, final_answer)

                    logger.success("对话持久化完成：user + assistant")
                except Exception as e:
                     logger.error(f"保存对话记忆异常: {e}\n{traceback.format_exc()}")


                return final_answer