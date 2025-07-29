import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver


from how_to.ai_agent.agent import Agent
from how_to.ai_agent.agent_tools import polygon_tools, wikipedia_tools, custom_tools
from how_to.ai_agent.system_prompt import return_system_prompt

import uuid

load_dotenv()
ABORT_VALUES = ("quit", "exit", "quit()", "exit()")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

## Instantiate all the tools
llm = init_chat_model(
    "gemini-2.0-flash",
    model_provider="google_genai",
    temperature=0,
)
tools = polygon_tools() + wikipedia_tools() + custom_tools()
memory = MemorySaver()
system_prompt = return_system_prompt()

agent = Agent(
    model = llm,
    tools = tools,
    memory=memory,
    system_prompt=system_prompt
)



def use_agent(user_message, thread_id: str ="abc123", debug: bool = False):
    response = agent.ask(user_message, thread_id, debug )
    return response


def main():
    print("\nWelcome! Type your questions below. Use `quit` or `exit` to stop.")
    print("\n> ", end="")

    while (query := input()).lower() not in ABORT_VALUES:
        print(use_agent(query))
        print("\n> ", end="")


if __name__ == "__main__":
    main()
