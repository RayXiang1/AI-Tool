from langchain import LLMChain
from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv,find_dotenv
import os
# Chat specific components
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory

load_dotenv(find_dotenv())
openai_api_key=os.getenv('OPENAI_API_KEY')

template = """
You are a chatbot that is helpful.
Your goal is to help the user.

{chat_history}
Human: {human_input}
Chatbot:"""

def chat(human_input: str) -> str:

    memory = ConversationBufferMemory(memory_key="chat_history")
    
    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], 
        template=template
    )
    
    llm_chain = LLMChain(
        llm=OpenAI(openai_api_key=openai_api_key), 
        prompt=prompt, 
        verbose=True, 
        memory=memory
    )

    response = llm_chain.predict(human_input=human_input)

    return response

def chatWithSummary(human_input: str) -> str:

    summary_memory = ConversationSummaryMemory(llm = OpenAI(), memory_key="chat_history")

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], 
        template=template
    )
    
    llm_chain = LLMChain(
        llm=OpenAI(openai_api_key=openai_api_key), 
        prompt=prompt, 
        verbose=True, 
        memory=summary_memory
    )

    response = llm_chain.predict(human_input=human_input)

    return response

# print(chatWithSummary(human_input = "I'm Bob?"))
# print(chat(chat_history = "Bob", human_input = "Are you Bob?"))

# print(chat(chat_history = "Ray", human_input = "Who are you?"))
# print(chat(chat_history = "Ray", human_input = "Are you Ray?"))
