from typing import Literal


def count_words(text: str) -> str:
    """Counts the number of words in the input text."""
    num_words = len(text.split())
    return f"The input contains {num_words} words."


def convert_celsius(
    celsius: float,
    to: Literal["Kelvin", "Fahrenheit"],
) -> float:
    """Converts Celsius to Kelvin or Fahrenheit."""
    if to == "Kelvin":
        return celsius + 273.15
    elif to == "Fahrenheit":
        return (celsius * 9 / 5) + 32
