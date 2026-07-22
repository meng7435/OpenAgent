import asyncio
from app.agnet.agent import Agent

async def main():
    agent = Agent()
    result  = await agent.run('介绍下你自己')
    print(result)

asyncio.run(main())