from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.llms import ollama

output_parser = CommaSeparatedListOutputParser
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions}
)

model = ollama(temperature=0)

_input = prompt.format(subject="冰淇淋口味")

output = model(_input)
output_parser.parse(output)