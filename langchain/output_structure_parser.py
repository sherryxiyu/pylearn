from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
from langchain.llms import ollama

response_schemas = [
    ResponseSchema(name="answer", description="回答用户的问题"),
    ResponseSchema(name="source", description="回答用户问题的来源，应为一个网站")
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template="尽可能回答用户的问题=\n{format_instructions}\n{question}",
    input_varibles=["question"],
    partical_variables={"format_instructions":format_instructions},
)

model=ollama(tempreature=0)

_input = prompt.format_prompt(question="法国的首都是？")
output = model(_input.to_string)
output_parser.parse(output)