from langchain.prompts import FewShotChatMessagePromptTemplate, ChatPromptTemplate
examples = [{"input": "2+2", "output": "4"},
            {"input": "2+3", "output": "5"},]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])
few_shot_prompt = FewShotChatMessagePromptTemplate(example_prompt=example_prompt, examples=examples)
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are wonderous wizard of match"),
    few_shot_prompt,
    ("human", "{input}"),
])
print(few_shot_prompt.format(input="what's 3+3?"))

from langchain.chat_models import ChatOllama
chain = final_prompt | ChatOllama(temperature=0.8)
chain.invoke({"input": "what's 3+3?"})
