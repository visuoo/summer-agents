import os
from dotenv import load_dotenv, dotenv_values 
from langchain_openai import ChatOpenAI
from langchain.memory import ChatMessageHistory

load_dotenv() 

class Dog:
    def __init__(self):
        self.name = None
        self.owner_name = None
        self.llm = ChatOpenAI(temperature=0)
        self.history = ChatMessageHistory()
        self.history.add_user_message("You are a robotic dog that will have a personal name who obeys his owners commands rember what your name is and what your owners name is")

    def __call__(self):
        human = input("say something to the dog")
        self.history.add_user_message(human)
        response = self.llm(self.history.messages)
        print(response.content)




    
x = Dog()
x()
print(x.name, x.owner_name)
x()

#dog name is xyz then you ask questions then another question dog whats your name