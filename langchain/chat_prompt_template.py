from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
human_prompt = "Summarize our conversation so far in {word_count} words"
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)
chat_prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name="conversation"), human_message_template])

from langchain.schema import HumanMessage, AIMessage
human_message = HumanMessage(content="what is the best way to learn programing?")
ai_message = AIMessage(content="1.choose a programming language:Decide on a programming language that you want to learn.")
print(chat_prompt.format_prompt(conversation=[human_message, ai_message], word_count=10).to_messages())