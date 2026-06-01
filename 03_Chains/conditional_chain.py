from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
# from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["Pos", "Neg"] = Field(
        description="Give me the sentiment of the feedback"
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classfy the sentiment of feedback of the text into Positive and Negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()},
)


classifier_chain = prompt1 | model | parser2
result = classifier_chain.invoke(
    {"feedback": "The animation of black clover is not that good"}
)

print(result)
