from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="tinyllama")
print("What would you like to ask about?: ")
question = str(input())
response = llm.invoke(question)
print(response)