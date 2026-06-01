from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()
model = ChatOpenAI()

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["Negative", "Positive"] = Field(
        description="Give the sentiment of feedback"
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="classify the sentiment of the {feedback} into text  \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()},
)
classify_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="write me an appropriate response to this Positive feedback \n {feedback}",
    input_variables=["feedback"],
)
prompt3 = PromptTemplate(
    template="write me an appropriate response to this Negative feedback\n{feedback}",
    input_variables=["feedback"],
)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find the sentiment"),
)
chain = classify_chain | branch_chain
result = chain.invoke({"feedback": "The deforestation is terrible thing"})

print(result)
