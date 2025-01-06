from langchain.llms import ollama
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class Actor(BaseModel):
    name: str = Field(discriminator="name of an actor")
    film_names: List[str] = Field(discription="list of names of films they starred in")

actor_query = "Generate the filmography for random actor"
parser = PydanticOutputParser(pydantic_object=Actor)
misformatted = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}" # 这是一个错误的json格式数据，因为其中的数据应该用双引号括起来

from langchain.output_parsers import OutputFixingParser

new_parser = OutputFixingParser.from_llm(parser=parser, llm=ollama())
new_parser.parse(misformatted)
# 这样就能直接修复错误的输出并reformat
