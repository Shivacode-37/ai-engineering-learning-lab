from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()
model = ChatOpenAI()


class person(BaseModel):
    name: str = Field(description=" The name of the person")
    age: int = Field(gt=15, description="The age of the person")
    city: str = Field(description="The name of the city it belongs to")


parser = PydanticOutputParser(pydantic_object=person)
template = PromptTemplate(
    template="Generate me the name, age , city of {anime} worls\n {format_instruction}",
    input_variables=["anime"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser

result = chain.invoke({"anime": "Black clover"})
print(result)
