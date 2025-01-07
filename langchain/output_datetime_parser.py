from langchain.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser
from langchain.chains import llm
from langchain_community.llms import Ollama

output_parser = DatetimeOutputParser()
template = """回答用户的问题：
{question}
{format_instructions}"""

prompt = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)
ollama_llm = Ollama(model="llama2-chinese", base_url="http://localhost:11434")
chain = llm.LLMChain(prompt=prompt, llm=ollama_llm)
output = chain.invoke({"question": "bitcoin是什么时候出现的？用%Y-%m-%dT%H:%M:%S.%fZ格式输出时间"})
print(output_parser.parse(output["text"]))
