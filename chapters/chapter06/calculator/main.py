import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


async def run():
    client = MultiServerMCPClient(
            {
                "calculator": {
                    "command": "uv",
                    "args": ["run", "server.py"],
                    "transport": "stdio"
                }
            }
        )

    tools = await client.get_tools()
    agent = create_react_agent(model, tools)
    
    while True:
        print("q: for quit")
        user = input("Questions: ")
        if user == "q":
            break
        math_response = await agent.ainvoke({"messages": user})
        print(math_response["messages"][-1].content)

asyncio.run(run())

# solve the following equation "[ ({(3*4)/4} + 10)/5  ]" also explain the steps you took to answer the question and which tool you used.
