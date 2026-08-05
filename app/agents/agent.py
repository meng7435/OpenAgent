import traceback
from logging import setLogRecordFactory

from jupyter_client.session import session_flags

from app.llm.client import LLMClient
from app.mcp.client import MCPClient
from app.mcp import server
import json
from app.memory.manager import MemoryManager
from loguru import logger
from app.planner.planner import Planner
from app.skills import skill_manager


class Agent:
    def __init__(self):
        self.llm = LLMClient()
        # mcp
        self.mcp = MCPClient(server)
        # skill
        self.skill = skill_manager
        self.memory = MemoryManager()
        self.planner = Planner(
            self.llm
        )

    async def run(self, user_msg, session_id):

        # 加载历史记录
        history = await self.memory.get_history(session_id)
        messages = [{"role": "system", "content": "你是一个AI Agent"}]
        valid_history = []
        for item in history:
            if isinstance(item, dict):
                valid_history.append(item)
        messages.extend(valid_history)
        user_input_msg = {"role": "user", "content": user_msg}
        messages.append(user_input_msg)

        # skill获取
        skill_tools = self.skill.get_schemas()
        plane = await self.planner.create_plan(messages, skill_tools)
        results = []
        for task in plane.tasks:
            logger.info(task)
            skill = self.skill.get(task.skill)
            if skill:
                result = await skill.execute(task.input['city'])
                results.append(
                    {

                        "skill":
                            task.skill,
                        "result":
                            result
                    }
                )
        final_answer = await self.summary(
            user_msg,
            results
        )
        assistant_msg = {
            "role": "assistant",
            "content": final_answer

        }
        try:
            # 短期记忆保存
            await self.memory.save_message(
                session_id,
                user_input_msg
            )
            await self.memory.save_message(
                session_id,
                assistant_msg
            )

            # 长期记忆保存
            await self.memory.save_user_memory( session_id,
                user_msg)
            await self.memory.save_user_memory( session_id,
                final_answer)
            logger.success(
                "对话保存成功"
            )


        except Exception:

            logger.error(
                traceback.format_exc()
            )

        return final_answer

    async def summary(
            self,
            question,
            results
    ):

        response = await self.llm.chat(

            [

                {
                    "role": "system",

                    "content":
                        """
                        根据执行结果回答用户。
                        不要提及内部Skill和工具。
                        """
                },

                {
                    "role": "user",

                    "content":
                        f"""
    用户问题:

    {question}


    执行结果:

    {results}

    """
                }

            ]

        )

        return response.content
