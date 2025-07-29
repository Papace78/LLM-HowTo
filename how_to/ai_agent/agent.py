from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.language_models.chat_models import BaseChatModel
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
            model=model, tools=tools, checkpointer=memory, prompt=system_prompt
        )

    def ask(self, query: str, conversation_id: str, debug: bool = False) -> str:
        config = {"configurable": {"thread_id": f"{conversation_id}"}}
        if debug:
            for step in self.agent.stream(
                {"messages": [HumanMessage(content=query)]},
                stream_mode="values",
                config=config,
            ):
                step["messages"][-1].pretty_print()
            return "Finished"
        response = self.agent.invoke(
            {"messages": [HumanMessage(content=query)]}, config=config
        )
        return response["messages"][-1].content


if __name__ == "__main__":
    from langchain.chat_models import init_chat_model

    llm = init_chat_model(
        model="gemini-2.0-flash", model_provider="google_genai", temperature=0
    )

    from langchain_community.agent_toolkits.polygon.toolkit import PolygonToolkit
    from langchain_community.utilities.polygon import PolygonAPIWrapper

    polygon = PolygonAPIWrapper()
    toolkit = PolygonToolkit.from_polygon_api_wrapper(polygon)
    polygon_tools = toolkit.get_tools()

    from langgraph.checkpoint.memory import MemorySaver

    memory = MemorySaver()

    from langgraph.prebuilt import create_react_agent

    agent = create_react_agent(
        model=llm,
        tools=polygon_tools,
        checkpointer=memory,
        prompt="you are an ai agent.",
    )

    agent_executor = Agent(
        model=llm,
        tools=polygon_tools,
        memory=memory,
        system_prompt="You are an AI agent.",
    )

    response = agent_executor.ask("How are you doing ?","abc12", debug=True)
    print(response)
