from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

chat_template = ChatPromptTemplate(
    [
        ("system", "You are expert in {Cars} technology "),
        ("human", "Tell me about {Bike}"),
    ]
)

prompt = chat_template.invoke({"Cars": "Range Rover", "Bike": "Triumph speed 400"})
print(prompt)
