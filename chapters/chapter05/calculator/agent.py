import os 
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from mcp_use import MCPAgent

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
model = init_chat_model("gemini-2.5-pro", model_provider="google_genai")

def make_agent(client) -> MCPAgent:
    return MCPAgent(
        llm=model,
        client=client,
        max_steps=30
    )