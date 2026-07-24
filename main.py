import asyncio
from app.agent.agent import Agent

async def main():
    agent = Agent()
    result = await agent.run('我叫张三',"user001")
    print(result)
    result = await agent.run(

        "我叫什么？",

        "user001"

    )
    print(result)

asyncio.run(main())