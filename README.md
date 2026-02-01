# 🦙 Ollama CLI Chatbot

A lightweight, streaming command-line interface (CLI) chatbot built using **Python**, **LangChain**, and **Ollama**.

This script establishes a conversational loop with a local Large Language Model (LLM), maintaining chat history context and streaming responses token-by-token for a real-time experience.

## ✨ Features

* **Local Privacy:** Runs entirely on your machine using Ollama.
* **Streaming Output:** text appears instantly as it is generated (no waiting for the full response).
* **Context Aware:** The bot remembers previous messages in the conversation session.
* **Simple Interface:** Clean CLI input/output loop.

## 🛠️ Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.8+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com).

## 🚀 Installation

### 1. Set up the Environment

Create a virtual environment (optional but recommended) and install the required LangChain packages:

```bash
pip install langchain-ollama langchain-core

```

### 2. Pull the Model

Ensure the Ollama server is running. You must pull the model specified in the code.

> **Note:** The code currently uses `gpt-oss:120b-cloud`. If you do not have this specific custom model, you should change the model name in the Python script or pull a standard model like Llama 3:

```bash
# Example for a standard model
ollama pull llama3

```

## 💻 Usage

1. Save the python script as `chatbot.py` (or any name you prefer).
2. Run the script:

```bash
python chatbot.py

```

3. Start chatting!
* Type your message and press Enter.
* Type `quit`, `exit`, or `q` to stop the program.



## ⚙️ Configuration

To change the model or the creativity of the AI, modify this line in your Python script:

```python
chat = ChatOllama(
    model="gpt-oss:120b-cloud",  # Change this to "llama3", "mistral", etc.
    temperature=0.7              # 0.0 = deterministic, 1.0 = creative
)

```

## 📝 Code Overview

* **`ChatOllama`**: The LangChain integration that communicates with the local Ollama server.
* **`chat_history`**: A list that stores `HumanMessage` and `AIMessage` objects to maintain conversation context.
* **`chat.stream`**: Generates the response in chunks, allowing for the "typewriter" effect in the terminal.

---

**License**
[MIT](https://choosealicense.com/licenses/mit/)

---
