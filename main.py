import asyncio

from app.agents import agent_manager
from app.agents.agent import Agent
from app.agents.supervisor import SupervisorAgent
from app.agents.system import MultiAgentSystem
from app.llm.client import LLMClient
from app.memory.long_memory import LongMemory
from app.agents.react_agent import ReactAgent

async def main():
    # agents = ReactAgent()
    # result = await agents.run(message="帮我规划上海三日游")
    # agent = Agent()
    # result = await agent.run("帮我规划上海三日游",'us1234')
    # print(result)

    #  Multi——Agent
    llm_instance = LLMClient()
    supervisor = SupervisorAgent(llm_instance,agent_manager)
    system = MultiAgentSystem(supervisor,agent_manager)
    result = await system.run(

        "分析某公司并生成报告"

    )

    print(result)
    # mem = LongMemory()
    # # 调高top_k，尽可能召回多条
    # contents = await mem.search(query="上海")
    # print("检索到的记忆内容：")
    # for c in contents:
    #     print("-", c)
asyncio.run(main())