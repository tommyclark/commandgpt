from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def getPromptedLLMChain():
    llm = OpenAI(temperature=.7)
    template = """You will return a bash command which meets the criteria set out in the question.
        You will return only the command and no other text.
        Question: {text}
        Answer:
        """
    prompt_template = PromptTemplate(input_variables=["text"], template=template)
    return LLMChain(llm, prompt_template)