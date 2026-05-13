from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

first_chatmodel = ChatOpenAI(model="gpt-4")

result = first_chatmodel.invoke("Who is Gojo Satoru?")
print(result.content)
