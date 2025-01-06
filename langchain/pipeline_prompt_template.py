# from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate
full_template = """
{introduction}
{example}
{start}
"""
full_prompt = PromptTemplate.from_template(full_template)

example_template = """here's an example of an interaction
Q:{example_q}
A:{example_a}
"""
example_prompt = PromptTemplate.from_template(example_template)

introduction_template = """you are impersonating {person}"""
introduction_prompt = PromptTemplate.from_template(introduction_template)

start_templete = """now do this for real
Q:{input}
A:"""
start_prompt = PromptTemplate.from_template(start_templete)

input_prompts = [
    ("introduction", introduction_prompt),
    ("example", example_prompt),
    ("start", start_prompt)
]

# pipeline_prompt = PipelinePromptTemplate(finxal_prompt=full_prompt, pipeline_prompts=input_prompts)

my_input = {"person":"teacher", "example_q":"what's apple?", "example_a":"apple is a kind of fruit", "input":"what's banana?"}
for name, prompt in input_prompts:
    my_input[name] = prompt.invoke(my_input).to_string()
my_output = full_prompt.invoke(my_input)
print(my_output)