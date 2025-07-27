"""Basic call to an LLM chatbot, one prompt at a time, with temperature control."""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()


class LLM_Model:
    def __init__(
        self,
        model_name: str = "gemini-2.0-flash",
        model_provider: str = "google_genai",
        temperature: float = 0.0,
        max_output_tokens: int | None = None,
        system_message: SystemMessage | str = SystemMessage(""),
    ) -> None:
        """Initialize the chosen LLM."""
        self.model_name = model_name
        self.model_provider = model_provider
        self.system_message = (
            system_message if isinstance(system_message, SystemMessage) else SystemMessage(system_message)
        )
        self._temperature = temperature
        self._max_output_tokens = max_output_tokens

        self.model = init_chat_model(
            model=model_name,
            model_provider=model_provider,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

    @property
    def temperature(self) -> float:
        return getattr(self.model, "temperature", self._temperature)

    @property
    def max_output_tokens(self) -> int | None:
        return getattr(self.model, "max_output_tokens", self._max_output_tokens)

    def prompt(
        self,
        system_message: str = "",
        human_message: str = "",
    ) -> str:
        """Send a prompt to the LLM and return the response."""
        print("\nPrompting...\n")
        if system_message:
            print(f"Context: {system_message}")
        print(f"Prompt:  {human_message}\n")

        response = self.model.invoke(
            [
                SystemMessage(system_message),
                HumanMessage(human_message),
            ]
        )
        return response.content

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
        if hasattr(self.model, "temperature"):
            self.model.temperature = temperature

    def set_max_output_tokens(self, max_output_tokens: int | None) -> None:
        self._max_output_tokens = max_output_tokens
        if hasattr(self.model, "max_output_tokens"):
            self.model.max_output_tokens = max_output_tokens


if __name__ == "__main__":
    config = {
        "model_name": "gemini-2.0-flash",
        "model_provider": "google_genai",
        "temperature": 0,
        "max_output_tokens": None,
    }

    model = LLM_Model(**config)

    print("\n</> LLM Model")
    print("-------------")
    print(f"model:            {model.model_name}")
    print(f"provider:         {model.model_provider}")
    print(f"temperature:      {model.temperature}")

    prompt = "How old is Paris?"

    print("\n-------")
    print("</> Basic API calling")
    print(model.prompt(human_message=prompt))

    print("\n-------")
    print("</> Creative API calling -> Temperature changed to 2!")
    model.set_temperature(2)
    for _ in range(3):
        print(model.prompt(human_message=prompt))

    print("\n-------")
    print("</> Uncreative API calling -> Temperature changed to 0!")
    model.set_temperature(0)
    for _ in range(3):
        print(model.prompt(human_message=prompt))

    print("\n-------")
    print("</> Let's make a social media post about it -> Add a context")

    system_message = (
        "You are a creative social media writer writing posts for a Gen AI student. "
        "Your posts always include a pun, and a call to action. "
        "Your posts are maximum 200 characters long. "
        "You always use emojis."
    )

    print(model.prompt(system_message=system_message, human_message=prompt))
