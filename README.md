# MCP Course
## Build Servers, Clients & Connect with Google Gemini Agents

- Chapter 1: Introduction to MCP
- Chapter 2: Environment Setup

**Project 1: Calculator**

- Chapter 3: Your First MCP Server
- Chapter 4: Your First MCP Client
- Chapter 5: Building Your First Gemini Agent
- Chapter 6: MCP Client & Agent using Langhain & LangGraph

**Project 2: Basic CLI Coder Like Gemini CLI**

- Chapter 7: File Management MCP Server
- Chapter 8: Advanced File Client
- Chapter 9: Gemini File Assistant
- Chapter 10: Agent Terminal Interface

**Milestone Checkpoints:**
- ✅ Week 1: Basic server and client working
- ✅ Week 2: Gemini successfully using your tools
- ✅ Week 3: Complex file operations through AI
- ✅ Week 4: Multiple servers integrated
- ✅ Week 6: Complete AI assistant system

---

### Chapter 1: Introduction to MCP
**What you'll learn:**
- What is Model Context Protocol and why it matters
- How MCP enables AI agents to use tools and access resources
- The three key components: Servers (tools), Clients (connectors), Hosts (AI agents)
- Real-world examples of MCP in action

**first understanding:**
- MCP is like a bridge that lets AI models (like Gemini) use external tools
- Think of it as giving your AI assistant the ability to use apps on your computer
- You'll build the tools (servers) and teach Gemini how to use them

### Chapter 2: Environment Setup
**Your development setup:**
- Python 3.8+ environment
- Google Gemini API key setup
- VS Code with Python extensions
- Basic project structure

**First success milestone:** Successfully connect to Gemini API and send a basic message

---

### Chapter 3: First MCP Server
**Project: Simple Calculator Server**

**What you'll build:**
- A basic MCP server that provides calculator tools
- Tools: add, subtract, multiply, divide
- Learn server registration and tool handling

**Learning outcomes:**
- Understand how MCP servers work
- Create and register tools
- Handle parameters and return results

### Chapter 4: Your First MCP Client
**Project: Basic MCP Client**

**What you'll build:**
- A simple client that connects to your calculator server
- Discover available tools
- Execute tool calls
- Handle responses

**Client will:**
- Connect to your calculator server
- List available tools (add, subtract, multiply, divide)
- Execute calculations
- Display results

**Milestone:** Successfully perform calculations using your MCP server through your client

---

### Chapter 5: Building Your First Gemini Agent
**Project: Gemini Calculator Agent**

**What you'll create:**
- A Gemini agent that can use your calculator server
- Natural language to tool execution
- Tool result interpretation

**Agent will handle requests like:**
- "Calculate 15 + 27"
- "What's 144 divided by 12?"
- "I need to multiply 8 by 7"

**Your first AI-powered tool interaction:** Watch Gemini understand natural language and execute your calculator tools

### Chapter 6: MCP Client & Agent using Langhain & LangGraph

**What you'll add:**
- MCP Client fro calculator server uing LangChain
- React Agent using LangGraph

**Your enhanced agent will:**
- MCP using LangChain & LangGraph 
- Handle complex multi-step problems

---

### Chapter 7: File Management MCP Server
**Project: Personal File Assistant**

**What you'll build:**
- File operations: create, read, update, delete
- Directory navigation
- File search capabilities
- Text file content manipulation

**Tools you'll implement:**
- `list_files(directory)` - List files in a directory
- `read_file(filepath)` - Read file contents
- `write_file(filepath, content)` - Write to file
- `search_files(pattern)` - Search for files
- `create_directory(path)` - Create directories

### Chapter 8: File Client
**Project: Personal File Assistant**

**What you'll create:**
- A sophisticated client for your file server
- File filtering and sorting
- Chat Memory

**Client features:**
- Connect to file server
- Execute complex file operations
- Handle large file lists
- Progress reporting

### Chapter 9: Gemini File Assistant
**Project: Personal File Assistant**

**What you'll build:**
- Gemini agent that manages files through natural language
- Automated file tasks

**Assistant will handle:**
- "Create a new folder called 'Projects' in my Documents"
- "Find all Python files in my current directory"
- "Read the contents of my todo.txt file"
- "Create a new file called 'notes.md' with today's date"

**Advanced features:**
- File content analysis
- Automatic file categorization

---
