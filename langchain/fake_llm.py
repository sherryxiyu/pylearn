from langchain.llms.fake import FakeListLLM

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

tools = load_tools(['python_repl'])
responses = ["Action: Python REPC\nAction Input: print(2+2)","Final Answer: 4"]

llm = FakeListLLM(responses=responses)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent.run("whats 2+2")

# wikipedia (pip install wikipedia)
import os
os.environ['http_proxy'] = 'http://127.0.0.1:10809'
os.environ['https_proxy'] = 'https://127.0.0.1:10809'

from langchain.llms.human import HumanInputLLM

tools = load_tools(['wikipedia'])

llm = HumanInputLLM(
    prompt_func=lambda prompt: print(
        f"\n===PROMPT====\n{prompt}\n===END OF PROMPT==="
    )
)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run("what is bocchi the rock!")