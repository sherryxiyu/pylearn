from langchain.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser
from langchain.chains import llm
from langchain.llms import ollama

output_parser = DatetimeOutputParser()
template = """回答用户的问题：
{question}
{format_instructions}"""

prompt = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

chain = llm(prompt=prompt, llm=ollama())

output = chain.run("bitcoin是什么时候出现的？用英文格式输出时间")

output_parser.parse(output)
