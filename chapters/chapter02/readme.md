# Chapter 2: Environment Setup
## Getting Development Tools Ready - Building AI Workshop


## What We're Setting Up Today 📋

By the end of this chapter, you'll have:
- ✅ Python 3.8+ installed and working
- ✅ Google Gemini API access configured
- ✅ VS Code editor with helpful extensions
- ✅ Your MCP project folder structure
- ✅ All the libraries you need for MCP development

**Milestone**: Send your first message to Google Gemini using Python code!

---

## Step 1: Installing Python 3.8+ 🐍

Python is the programming language we'll use throughout this course. It's beginner-friendly and perfect for AI development.

### Check if Python is Already Installed

First, let's see if Python is already on your computer:

**On Windows:**
1. Press `Windows + R`
2. Type `cmd` and press Enter
3. Type `python --version` and press Enter

**On Mac:**
1. Press `Cmd + Space` to open Spotlight
2. Type `Terminal` and press Enter
3. Type `python3 --version` and press Enter

**On Linux:**
1. Open Terminal (usually `Ctrl + Alt + T`)
2. Type `python3 --version` and press Enter

### What You Should See
If Python is installed, you'll see something like:
```
Python 3.9.7
```
or
```
Python 3.11.2
```

**If you see version 3.8 or higher** - Great! You're ready to go!

**If you see version 3.7 or lower, or get an error** - You need to install Python.

### Installing Python (If Needed)

**Windows:**
1. Go to [python.org/downloads](https://python.org/downloads)
2. Click "Download Python 3.11.x" (or latest version)
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" during installation
5. Click "Install Now"

**Mac:**
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download the macOS installer
3. Run the installer and follow the prompts

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Verify Your Installation
After installation, close and reopen your terminal/command prompt, then run:
```bash
python --version
```
or
```bash
python3 --version
```

You should see Python 3.8+ listed!

---

## Step 2: Setting Up Google Gemini API 🤖

Now let's get access to Google Gemini, the AI model that will use your MCP tools.

### Getting Your API Key

1. **Go to Google AI Studio**
   - Visit: [aistudio.google.com](https://aistudio.google.com)
   - Sign in with your Google account

2. **Create a New API Key**
   - Click "Get API Key" or "Create API Key"
   - Choose "Create API key in new project" (recommended)
   - Copy the API key that appears
   - **IMPORTANT**: Save this key somewhere safe - you'll need it!

### Your API Key Looks Like This:
```
AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Safety Note 🔒
- Never share your API key with anyone
- Don't post it online or in public repositories
- Treat it like a password - it's your personal access to Gemini

---

## Step 3: Installing VS Code - Your Code Editor 💻

VS Code (Visual Studio Code) is a free, powerful code editor that makes programming much easier.

### Download and Install VS Code

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Click "Download for [Your Operating System]"
3. Run the installer
4. Follow the installation prompts

### Essential Extensions for Python Development

After VS Code is installed:

1. **Open VS Code**
2. **Install Python Extension**:
   - Click the Extensions icon (square icon on the left sidebar)
   - Search for "Python"
   - Install the official Python extension by Microsoft

3. **Install Additional Helpful Extensions**:
   - **Python Docstring Generator**: Helps write code documentation
   - **Code Runner**: Run code snippets quickly
   - **Material Icon Theme**: Makes files easier to identify

### Configure VS Code for Python

1. **Open VS Code**
2. **Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)**
3. **Type "Python: Select Interpreter"**
4. **Choose your Python installation** (should show Python 3.8+)

---

## Step 4: Creating Your Project Structure 📁

Let's create a organized folder structure for your MCP projects.

### Create Your Main Project Folder

1. **Create a new folder** called `mcp-course` on your desktop or in your documents
2. **Open VS Code**
3. **File → Open Folder**
4. **Select your `mcp-course` folder**


## Step 5: Installing Required Libraries 📚

Now let's install the Python libraries we need for MCP development.

### Create Requirements File

In your `mcp-course` folder, create a file called `requirements.txt` with this content:

```text
google-generativeai==0.3.2
mcp==0.1.0
asyncio-mqtt==0.13.0
python-dotenv==1.0.0
requests==2.31.0
```

### Install the Libraries

1. **Open Terminal in VS Code**:
   - Go to `Terminal → New Terminal`
   - You should see a terminal at the bottom of VS Code

2. **Install the libraries**:
   ```bash
   uv add -r requirements.txt
   ```

3. **Wait for installation to complete**
   - You'll see various libraries being downloaded and installed
   - This might take a few minutes

---