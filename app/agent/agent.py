import traceback
from logging import setLogRecordFactory

from app.llm.client import LLMClient
from app.mcp.client import MCPClient
from app.mcp import server
from app.tools import create_tool_manager
import json
from app.memory.manager import MemoryManager
from loguru import logger
from app.skills import skill_manager
class Agent:
    def __init__(self):
        self.llm = LLMClient()
        # mcp
        self.mcp = MCPClient(server)
        # skill
        self.skill = skill_manager
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
        # skill获取
        skill_tools = self.skill.get_schemas()
        logger.info(skill_tools)
        tools = skill_tools
        while True:
            response = await self.llm.chat(messages, tools)
            if response.tool_calls:
                assistant_call_msg = response.model_dump(mode="json")
                messages.append(assistant_call_msg)

                for call in response.tool_calls:
                    name = call.function.name
                    arguments = json.loads(call.function.arguments)
                    logger.info(f"收到技能调用：{name}, 参数={arguments}")

                    skill = self.skill.get(name)
                    if not skill:
                        err_info = f"错误：不存在技能【{name}】"
                        logger.error(err_info)
                        tool_msg = {
                            "role": "tool",
                            "tool_call_id": call.id,
                            "content": err_info
                        }
                        messages.append(tool_msg)
                        continue

                    logger.info(f"开始执行Skill:{name}")
                    result = await skill.execute(arguments)

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