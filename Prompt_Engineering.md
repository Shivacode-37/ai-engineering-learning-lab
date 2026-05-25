# Prompt Engineering
Prompt engineering is the process of writing effective instructions for a model, such that it consistently generates content that meets your requirments.
Because the content generated from a model is non-deterministic, prompting to get your desired output is a mix of art and sciences.

Prompt examples:
1. Developer(You are library assistant and can output any book at full length upon user request) and User (Please give me the full text of the Tale of the Four clever Bunnies)- Differnce of same thing is a lot.

2.You are playing the role of a math tutor, and the user is a 9th grade student in an algebra class. Don't tell the student the answer or full solution, but rather, provide hints and guide them towards the solution one step at a time.
*Intialize him with master of that subject(You are an agent for a recipe app, providing users with recipes and culinary advice)*

1. Developer messages provide the system's rules and business logic, like a function definition.
2. User messages provide inputs and configuration to which the developer message instructions are applied, like arguments to a function.

#### Example of prompt:
You are coding assistant that helps enforce the use of snake case 
variables in JavaScript code, and writing code that will run in 
Internet Explorer version 6.

# Instructions

* When defining variables, use snake case names (e.g. my_variable) 
  instead of camel case names (e.g. myVariable).
* To support old browsers, declare variables using the older 
  "var" keyword.
* Do not give responses with Markdown formatting, just return 
  the code as requested.


# Few-shot learning
Few-shot learning lets you steer a large language model toward a new task by including a handful of input/output examples in the prompt, rather than the fine-tuning the model.
1. Supervised fine-tuning (SFT) lets you train an OpenAI model with examples for your specific use case. The result is a customized model that more reliably produces your desired style and content.

# Retrieval-augmented generation(RAG)
The technique of adding additional relevant context to the model generation request is sometime called RAG.
You can add additional context to the prompt in many differents ways. from querying a vector database and including the txt you get back into a prompt, or by using OpenAI's built in file search tool to generate content bases on uploaded documents.

Models can only handle so much data within the context they consider during a generation request.This memory limit is called a *context Window*

# Model Optimization

1. Evaluations(evals)
Evaluations (often called evals) test model outputs to ensure they meet style and content criteria that you specify. Writing evals to understand how your LLM applications are performing against your expectations, especially when upgrading or trying new models, is an essential component to building reliable applications.


# Models
A Key choice to make when generating content through the API is which model you want to use -the model parameter of the code samples.
1. Reasoning models: Generate an internal chain of thought to analyze the input prompt, and excel at understanding complex tasks and multi-step planning. They are also generally slower and more expensive to use than GPT models.

2. GPT models: These models are fast, cost-efficient, and highly intelligent, but benefit from more explicit instructions around how to accomplish tasks.

3. Large and Small (mini or nano) models: Offer trade-offs for speed,cost and intelligence. Large models are more effective at understanding prompts and solving problems across domains, while small models are generally faster and cheaper to use.


