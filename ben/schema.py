from typing import Optional
import os
from dotenv import load_dotenv, dotenv_values 
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.memory import ChatMessageHistory


load_dotenv() 
class Dog(BaseModel):
    """Information about a dog."""

    # ^ Doc-string for the entity Dog.
    # This doc-string is sent to the LLM as the description of the schema Person,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    name: Optional[str] = Field(default=None, description="The name of the dog")
    owner_name: Optional[str] = Field(
        default=None, description="The name of the owner of the dog"
    )
    activity: Optional[str] = Field(default=None, description="The activity the dog should do. Limit this activity to: [walk, trick, sit], if it does not fit in one of these categories reject the activity")
    



class RobotDog:
    def __init__(self) -> None:
        self.name = None
        self.owner_name = None
        self.activity = None
        self.llm = ChatOpenAI(temperature=0)
        self.history = ChatMessageHistory()
        self.history.add_user_message("You are a robotic dog that will have a personal name who obeys his owners commands rember what your name is and what your owners name is")
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert extraction algorithm. "
                    "Only extract relevant information from the text. "
                    "If you do not know the value of an attribute asked to extract, "
                    "return null for the attribute's value.",
                ),
                # Please see the how-to about improving performance with
                # reference examples.
                # MessagesPlaceholder('examples'),
                ("human", "{text}"),
            ]
        )
        self.runnable = self.prompt | self.llm.with_structured_output(schema=Dog)
        
    def __call__(self):
        human = input("say something to the dog: ")
        self.history.add_user_message(human)
        response = self.llm(self.history.messages)
        print(response.content)
        data = self.runnable.invoke({"text": human})
        self.name = data.name
        self.owner_name = data.owner_name
        self.activity = data.activity 
        if(self.activity is not None):
            print(("The dog" or self.name) + " is doing " + self.activity)
        self.activity = None
        
doggy = RobotDog()
doggy()
print(doggy.name, doggy.owner_name, doggy.activity )
doggy()
print(doggy.name, doggy.owner_name, doggy.activity )
