from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Anime name is "{user_input}" Write me the characterstics of this anime:
Key Details:
The name of main character of anime
Explanation : "{Power}" of anime character """,
    input_variables=["user_input", "Power"],
    validate_template=True,
)
template.save("template.json")
