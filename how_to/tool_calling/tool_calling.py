from dotenv import load_dotenv
from typing import Literal

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.language_models.chat_models import BaseChatModel


from how_to.tool_calling.func_to_call import convert_celsius, count_words

load_dotenv()


@tool(parse_docstring=True)
def count_words_tool(text: str) -> str:
    """
    Count the number of words in a given text.

    This function takes a string input, counts the number of words, and
    returns a message with the total count.

    Args:
        text: The input text to count words from.

    Returns:
        A string detailing the number of words in the text.
    """
    return count_words(text)

@tool(parse_docstring=True)
def convert_celsius_tool(
    celsius: float,
    to: Literal["Kelvin", "Fahrenheit"],
) -> float:
    """
    Convert a temperature from Celsius to either Kelvin or Fahrenheit.

    This tool accepts a temperature in degrees Celsius and a target unit
    ("Kelvin" or "Fahrenheit"). It returns the converted temperature as a float.

    Args:
        celsius: The input temperature in degrees Celsius.
        to: A str containing one target unit: either "Kelvin" or "Fahrenheit".

    Returns:
        The converted temperature in the specified unit.

    Example:
        convert_celsius(celsius=100, to=["Fahrenheit"]) -> 212.0
    """
    return convert_celsius(celsius, to)


def llm_with_tools(
    tools: list[str],
    model_name: str = "gemini-2.0-flash",
    model_provider: str = "google_genai",
) -> BaseChatModel:
    llm = init_chat_model(
        model=model_name,
        model_provider=model_provider,
        temperature=0,
    )

    return llm.bind_tools(tools)



if __name__ == "__main__":
    # Initialize the chat model with tool support
    llm = llm_with_tools([count_words_tool, convert_celsius_tool])

    # First query: count words
    query = "How much word is in this text: 'Lorem ipsum badabum badabam' ?"
    response = llm.invoke(query)
    tool_called = response.tool_calls[0]["name"]
    args = response.tool_calls[0]["args"]
    print("\n</> Query:", query)
    print("Tool called:", tool_called)
    print("Args:", args)
    print("Answer:", count_words_tool.invoke(args))

    # Second query: convert Celsius to Fahrenheit
    query = "God it's hot. It's almost 9000° Celsius here! How much fahrenheit is that?"
    response = llm.invoke(query)
    tool_called = response.tool_calls[0]["name"]
    args = response.tool_calls[0]["args"]
    print("\n</> Query:", query)
    print("Tool called:", tool_called)
    print("Args:", args)
    print("Answer:", convert_celsius_tool.invoke(args))

    # Third query: convert Celsius to Kelvin
    query = "Water freezes at 0 degree celsius. Tell me when water freezes in Kelvin."
    response = llm.invoke(query)
    tool_called = response.tool_calls[0]["name"]
    args = response.tool_calls[0]["args"]
    print("\n</> Query:", query)
    print("Tool called:", tool_called)
    print("Args:", args)
    print("Answer:", convert_celsius_tool.invoke(args))
