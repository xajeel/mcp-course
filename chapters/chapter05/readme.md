# Chapter 5: Building First Agent

## What Are AI Agents? 

Before we dive into building our agent, let's understand what AI agents actually are and why they're revolutionizing how we interact with computers.

### Understanding AI Agents

Think of an AI agent as a digital assistant that can think, plan, and act on your behalf. Unlike traditional computer programs that follow fixed instructions, AI agents can:

- **Understand** what you want to achieve
- **Plan** how to accomplish your goals
- **Use tools** to get things done
- **Learn** from their experiences
- **Adapt** to new situations

### Real-World Examples You Might Know

**Virtual Assistants**: Siri, Alexa, and Google Assistant are AI agents. When you ask "What's the weather like?", they understand your question, use weather tools to get information, and provide you with an answer.

**Game Characters**: The NPCs (non-player characters) in modern video games are AI agents. They can make decisions, react to your actions, and pursue their own goals.

**Recommendation Systems**: Netflix's recommendation engine is an AI agent that studies your viewing habits and suggests movies you might like.

**Chatbots**: Customer service bots on websites are AI agents that can understand your problems and help solve them.

### How AI Agents Think

AI agents follow a simple cycle:
1. **Perceive**: They gather information about their environment
2. **Think**: They analyze the situation and decide what to do
3. **Act**: They take action using available tools
4. **Learn**: They remember what worked and what didn't

### Why Are AI Agents Powerful?

**Autonomy**: They can work independently without constant human supervision.

**Tool Usage**: They can use external tools like calculators, databases, or APIs to accomplish tasks.

**Multi-step Reasoning**: They can break down complex problems into smaller, manageable steps.

**Adaptability**: They can handle unexpected situations and adjust their approach.

### Types of AI Agents

**Reactive Agents**: Simple agents that respond to immediate situations (like a thermostat)

**Goal-Based Agents**: Agents that work toward specific objectives (like a GPS navigation system)

**Learning Agents**: Agents that improve their performance over time (like recommendation systems)

**Multi-Agent Systems**: Multiple agents working together (like a team of robots in a warehouse)

## Project Structure

Our calculator folder looks like this now:

```
calculator/
├── server.py          # MCP server implementation
├── client.py          # MCP client connection logic
├── agent.py           # Gemini agent configuration
└── main.py            # Application entry point
```

This separation of concerns makes our code maintainable and allows for easy testing and extension.

## Setting Up the Agent Configuration

The heart of our Gemini agent lies in the `agent.py` file. This module handles the initialization and configuration of our LLM.

### Key Components

**Environment Setup**: We use `python-dotenv` to manage our API keys securely. This keeps sensitive information out of our source code.

**Model Initialization**: We initialize the Gemini 2.5 flash model using LangChain's `init_chat_model`.

**Agent Factory**: The `make_agent` function creates an `MCPAgent` instance configured with:
- Our Gemini model for language understanding and generation
- An MCP client for tool communication
- A maximum of 30 steps to prevent infinite loops

### Code Breakdown

```python
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
```

The `max_steps` parameter is crucial for production systems. It prevents runaway execution while allowing complex multi-step reasoning.

## Understanding the Main Application Flow

Our `main.py` file orchestrates the entire application flow:

### Execution Pipeline

1. **Client Initialization**: Creates and configures the MCP client connection
2. **Agent Creation**: Instantiates the Gemini agent with the connected client
3. **Task Execution**: Runs a complex mathematical problem
4. **Result Display**: Shows both the answer and the reasoning process

### The Test Problem

Wecan pass multi-step mathematical expression: `((2 + 3) / 2)*4`

This problem tests several capabilities:
- **Order of Operations**: The agent must follow PEMDAS/BODMAS rules
- **Tool Usage**: It needs to use calculator functions through MCP
- **Explanation**: It should provide step-by-step reasoning

### Code Analysis

```python
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
```

The asynchronous design ensures our application can handle multiple concurrent operations efficiently.

## How the Agent Works

### Step-by-Step Process

1. **Problem Analysis**: The agent analyzes the mathematical expression and identifies the required operations
2. **Tool Discovery**: It queries the MCP server to understand available calculator functions
3. **Execution Planning**: The agent creates a plan to solve the problem step-by-step
4. **Tool Invocation**: It calls calculator functions through the MCP protocol
5. **Result Integration**: The agent combines results and provides explanations

### Expected Output

When you run this agent, you'll see output similar to:

[image](../../assets/chapter05-output.png)


## Running Agent

To execute your Gemini agent:

1. Ensure you have your Google API key in your `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Make sure your calculator MCP server is running

3. Execute the main application:
   ```bash
   uv run main.py
   ```


This foundational setup provides the building blocks for creating powerful, tool-enabled AI agents that can solve real-world problems through the Model Context Protocol.

## Summary

You've successfully created a Gemini agent that can:
- Connect to MCP servers
- Use external tools intelligently
- Provide detailed reasoning
- Handle complex multi-step problems

This architecture serves as the foundation for building more sophisticated AI systems that can interact with a wide variety of external tools and services through the standardized MCP protocol.