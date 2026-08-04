import asyncio
from app.agent.agent import Agent
from app.memory.long_memory import LongMemory
from app.agent.react_agent import ReactAgent
async def main():
    # agent = ReactAgent()
    # result = await agent.run(message="帮我规划上海三日游")
    agent = Agent()
    result = await agent.run("帮我规划上海三日游",'us1234')

    print(result)

    # mem = LongMemory()
    # # 调高top_k，尽可能召回多条
    # contents = await mem.search(query="上海")
    # print("检索到的记忆内容：")
    # for c in contents:
    #     print("-", c)
asyncio.run(main())