from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template="Write me 5 lines on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="write me 3 important bullet points{text}", input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "Langchain"})
print(result)
