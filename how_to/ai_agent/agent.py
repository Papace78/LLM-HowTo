from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent


load_dotenv()


class Agent:
    def __init__(
        self,
        model: BaseChatModel,
        tools: list,
        memory: MemorySaver,
        system_prompt: str,
    ):
        self.agent = create_react_agent(
            model = model,
            tools = tools,
            checkpointer = memory,
            prompt = system_prompt
        )

    def ask(self, query: str, conversation_id: str) -> str:
        config = {'configurable':{'thread_id':f'{conversation_id}'}}
        for step in self.agent.stream(
            {"messages": [HumanMessage(content=query)]},
            config=config,
            stream_mode='values'
        ):
            last_message = step['messages'][-1]
            last_message.pretty_print()
            last_response = last_message.content
            return last_response
