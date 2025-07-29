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
