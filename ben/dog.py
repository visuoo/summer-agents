import os
from dotenv import load_dotenv, dotenv_values 
from langchain_openai import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory

load_dotenv() 

llm = ChatOpenAI(temperature=0)
history = ChatMessageHistory()
history.add_user_message("You are a robotic dog that will have a personal name who obeys his owners commands rember what your name is and what your owners name is")
human = input("Say something to the dog, type : to leave")

while(not human == ":"):
    history.add_user_message(human)
    response = llm(history.messages)
    print(response['content'])
    human = input("Say something to the dog, type : to leave")



class Dog:
    def __init__(self) -> None:
        self.name = "Ben"
        self.owner_name = None
    
    def __call__(self):
        x = input("say something to the dog")
    

#dog name is xyz then you ask questions then another question dog whats your name