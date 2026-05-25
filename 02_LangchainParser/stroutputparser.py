from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template="Write me today current affairs on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="3 lines summary of {text}", input_variables=["text"]
)

prompt1 = template1.invoke({"topic": "IPL"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
result1 = model.invoke(prompt2)

print(result1.content)
