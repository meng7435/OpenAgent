import asyncio
from app.agent.agent import Agent

async def main():
    agent = Agent()
    result  = await agent.run('帮我查一下天气')
    print(result)

asyncio.run(main())