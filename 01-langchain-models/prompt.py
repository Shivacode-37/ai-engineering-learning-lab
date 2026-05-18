from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Temperature values provides the deterministic or randomness in output. If temperature is 0 it shows same output.

model = ChatOpenAI(model="gpt-4", temperature=0.1)

template1 = PromptTemplate(
    template=""" Recommend the user best top 5  anime: "{Name}"  """,
    input_variables=["Name"],
)
# fill the values
prompt = template1.invoke({"Name": "Dragon BallZ"})
result = model.invoke(prompt)
print(result.content)
