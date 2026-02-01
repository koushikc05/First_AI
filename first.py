from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


chat = ChatOllama(model="gpt-oss:120b-cloud", temperature=0.7)


chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

print("--- Start Chatting with Ollama (type 'quit' to exit) ---")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["quit", "exit", "q"]:
        break

    chat_history.append(HumanMessage(content=user_input))
  
    print("AI: ", end="", flush=True)
    response_content = ""
    
    for chunk in chat.stream(chat_history):
        print(chunk.content, end="", flush=True)
        response_content += chunk.content
    
    print() 
    chat_history.append(AIMessage(content=response_content))