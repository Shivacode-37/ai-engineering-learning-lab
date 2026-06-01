from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model1 = ChatOpenAI()
# model2 = ChatAnthropic(model_name= 'claude opus 4.7')

prompt1 = PromptTemplate(
    template="Generate the detailed notes of text {text}", input_variables=["text"]
)
prompt2 = PromptTemplate(
    template="write me 5 questions of notes for quiz \n from {text}",
    input_variables=["text"],
)
prompt3 = PromptTemplate(
    template="Merege the notes and 5 questions of quiz{notes} -> & \n {quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {"notes": prompt1 | model1 | parser, "quiz": prompt2 | model2 | parser}
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """ Agentic AI is a type of AI system that can autonomously make decisions, plan actions and execute tasks to achieve specific goals with minimal human intervention. It focuses on goal-driven behavior, reasoning and interaction with tools and environments.

Specialised mastery: It’s trained and fine-tuned to handle a particular type of problem with great accuracy.
Tool usage: It can connect with and use specific tools like software, APIs, databases, etc to achieve its goal.
Goal-oriented actions: Instead of just giving information, it actively takes steps toward completing the task.
Efficient problem-solving: Because it can plan, adapt and take actions autonomously, it can handle tasks more efficiently in dynamic environments.
Traditional vs. Agentic AI: Unlike traditional AI systems that primarily respond to inputs, Agentic AI focuses on autonomous decision-making and goal-driven actions. It is defined by behavior (how it acts), not by the breadth of knowledge like General AI."""

result = chain.invoke({"text": text})
print(result)
