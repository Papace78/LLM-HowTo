# 🤖 AI Agent

This folder shows how to build an **AI Agent** using [LangGraph](https://github.com/langchain-ai/langgraph), a framework built on top of LangChain.

## 🧠 What’s an Agent?

Unlike a regular LLM that just answers your prompt, an **agent** can:
- **Choose tools** to call based on your request
- **Run those tools automatically**
- **Use memory** to follow up over multiple steps
- **Decide what to do next**

You ask in natural language, and the agent handles the logic, calls APIs, gathers info, and returns results — step by step.

## 🚀 What can this one do?

This agent can:
- Get stock prices using the Polygon API
- Search Wikipedia

It’s like a smart assistant that *thinks*, *decides*, and *acts* — not just replies.

## Agent = Brain + Body + Memory + Education

| Component    | Description                                                                 | Analogy         |
|--------------|-----------------------------------------------------------------------------|-----------------|
| 🧠 Brain     | The **LLM model** (e.g. GPT-4, Claude) — the reasoning engine               | Intelligence    |
| 🛠️ Body      | The **Tools** the agent can call to interact with the world (APIs, scripts) | Muscles/Actions |
| 💾 Memory    | Persistent storage for conversation or state (e.g. `MemorySaver`)           | Long-term memory|
| 📚 Education | The system prompt or instructions defining the agent's role and goals       | Training/Personality |

---


## Usage

Run the AI agent CLI with:

```bash
uv run how_to/ai_agent/cli.py
```

```bash
Welcome! Type your questions below. Use `quit` or `exit` to stop.

> Who is the chancellor of Germany ?
The current officeholder is Friedrich Merz of the Christian Democratic Union, sworn in on 6 May 2025.

> What did I just ask ?
You asked who the chancellor of Germany is.

> What is the current apple stock market price ? as of today.
The closing price for Apple stock (AAPL) on July 28, 2025 was $214.05.

> Why did you give me July 28 ? I wanted today.
My apologies. I attempted to get today's stock price, but my access to real-time data is limited and I am not authorized to get the current price. Therefore, as per my instructions, I automatically defaulted to providing the last working day's closing price, which was July 28, 2025.
```
