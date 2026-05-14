from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template=""" Recommend the user best top 5  anime: "{Name}"  """,
    input_variables=["Name"],
)
# fill the values
prompt = template1.invoke({"Name": "Black Clover"})
result = model.invoke(prompt)
print(result.content)
