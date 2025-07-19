from client import make_client
from agent import make_agent
import asyncio

async def main():
    client = make_client()
    agent = make_agent(client)

    result = await agent.run("solve the following problem: ((2 + 3) / 2)*4 and also explain the process")
    print("======")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())