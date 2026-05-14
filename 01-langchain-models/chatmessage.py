from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are Neflix webseries specialist"),
    HumanMessage(content="Suggest me best Action Thriller Webseries "),
]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
