from app.llm.client import LLMClient
from app.skills import skill_manager
from app.state.agent_state import AgentState

from app.agents.action import AgentAction
import json
from app.prompts.react import react_prompt
from loguru import logger

class ReactAgent:
    def __init__(self):
        self.llm = LLMClient()
        self.skill_manager = skill_manager

    async def execute(
            self,
            action
    ):

        skill = self.skill_manager.get(
            action.action
        )

        if not skill:
            return {

                "error":
                    "Skill不存在"

            }
        result = await skill.execute(

            **action.input

        )

        return result

    async def run(self, message):
        state = AgentState(message)
        skill = self.skill_manager.get_schemas()
        while not state.finished:
            if len(state.step) > 5:
                return "任务执行超时"


            prompt = react_prompt(state.message,state.step,skill)
            message = [
                {'role':'system','content':prompt},
            ]
            response = await self.llm.chat(message)

            action_data = json.loads(response.content)

            if action_data['action'] == "finish":
                state.finished = True

                state.answer = action_data['input']

                break

            action = AgentAction(**action_data)

            state.step.append({
                "action": action.action,

                "input": action.input

            })


            # 调用SKILL
            logger.info(action)
            result = await self.execute(

                action

            )

            state.step.append(

                {
                    "observation": result
                }

            )

        return state.answer
