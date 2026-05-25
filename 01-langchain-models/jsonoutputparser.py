from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    JsonOutputParser,
    StructuredOutputParser,
    ResponseSchema,
)


load_dotenv()

model = ChatOpenAI()
parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Write me some facts about{topic} \n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template1 | model | parser

result = chain.invoke({"topic": "Badminton Racquet"})
print(result)


# --> Structured output parser
schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template="Write me some facts about{topic} \n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template1 | model | parser

result = chain.invoke({"topic": "Badminton Racquet"})
print(result)
