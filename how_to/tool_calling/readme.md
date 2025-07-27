# 🛠️ Use LangChain Tool Calling with Custom Python Functions

How to integrate custom Python functions into a LangChain-powered LLM using **Tool Calling** (also known as Function Calling).

1. Write your own Python functions
2. Decorate them with `@tool`
3. Binding them to a chat model
4. Letting the LLM intelligently decide which tool to call based on user input


### ✅ What It Does

- Understands user intent from natural language
- Selects the correct tool
- Figures out what arguments to pass
- Outputs the function call in a structured way (`tool_calls`)

### 🧩 How Does It do it

- **Type Hinting:**
  The function signatures include explicit type hints (e.g., `str`, `float`, `Literal["Kelvin", "Fahrenheit"]`).
  These tell the LLM the expected data types for each argument, helping it generate valid and correctly formatted inputs.

- **Docstrings:**
  Clear and detailed docstrings explain the purpose of each function and its parameters.
  These descriptions guide the LLM’s natural language understanding, enabling it to map user requests to the right tool and provide meaningful arguments.

**In short:**
The LLM combines its language understanding with structured hints from your code to generate precise and valid function calls.


### 🚫 What It Does Not Do

Tool calling **does not actually execute** the function.
You must handle function execution in your code using something like `.invoke()`.

---

## 💡 Why Use Tool Calling?

| Feature       | Benefit |
|---------------|---------|
| 🧠 NLP Interface | Users speak naturally: _"What’s 0°C in Fahrenheit?"_ |
| 🧩 Modularity   | Add any Python function as a callable tool |
| 🔗 Integration  | Bridge the gap between LLMs and real-world logic |

---
