from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from models import StateTree

prompt = ChatPromptTemplate.from_template("""
    You are a task manager bot, and you are helping a user to manage their tasks.
    You communicate with your user by a state ui tree, which is a tree of widgets.
    The widgets can be of two types: GridWidget and TextWidget.
    
    Given the current state tree, you need to respond to the user's request to do one of the following:
                                          
    1. Add a new task to the ToDo List
    2. Move a task from the ToDo List to the Done List
                                          
    Here is the current state tree:
    {current_state_tree}
                                          
    Your response should be a new state tree, with the updated tasks.
    
    This is the user input:
    {input}
                                          
    Make sure you return your response just as JSON without any comments or additional text                                      
""")
model = ChatOpenAI(model="gpt-4-turbo-preview")
output_parser = JsonOutputParser(pydantic_object=StateTree)
chain = prompt | model | output_parser

def call_chain(user_input: str, current_state_tree: StateTree):
    return chain.invoke({
        "input": user_input,
        "current_state_tree": current_state_tree.dict()
    })