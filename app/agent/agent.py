from app.llm.client import LLMClient
from app.agent.state import AgentState
from app.agent.parser import parse_action


class Agent:
    def __init__(self):
        self.llm = LLMClient()

    async def think(self, state: AgentState):
        result = await self.llm.chat(

            state.messages

        )

        state.messages.append(

            {

                "role": "assistant",

                "content": result

            }

        )

        return result

    async def run(self, user_message: str):
        state = AgentState()
        state.messages.append({
            "role": "system",

            "content":
                """
                你是一个AI Agent。

                你需要决定下一步行动。

                如果可以直接回答：

                返回:

                {
                    "action":"finish",
                    "input":"答案"
                }


                如果需要工具：

                返回:

                {
                    "action":"tool名称",
                    "input":"参数"
                }

                """

        })
        state.messages.append(

            {
                "role": "user",

                "content": user_message

            }

        )
        while not state.finished:
            state.iteration += 1
            print(
                f"\n=== 第{state.iteration}轮思考 ==="
            )
            response = await self.think(
                state
            )

            print(
                "LLM:",
                response
            )
            action = parse_action(response)
            print(
                "Action:",
                action
            )

            if action["action"] == "finish":

                state.finished = True

                return action["input"]

            else:

                # 暂时模拟工具
                observation = (
                    f"执行工具:"
                    f"{action['action']}"
                    f", 参数:"
                    f"{action['input']}"
                )
                state.messages.append(

                    {
                        "role": "tool",

                        "content": observation

                    }

                )
            return "结束"
