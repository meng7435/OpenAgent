import asyncio
from app.agent.agent import Agent
from app.memory.long_memory import LongMemory
async def main():
    agent = Agent()
    result = await agent.run('今天襄阳天气',"user001")
    print(result)
    result = await agent.run(

        "明天武汉天气？",

        "user001"

    )
    print(result)

    # main.py 调试代码
    mem = LongMemory()
    # 调高top_k，尽可能召回多条
    contents = await mem.search(query="天气")
    print("检索到的记忆内容：")
    for c in contents:
        print("-", c)
asyncio.run(main())