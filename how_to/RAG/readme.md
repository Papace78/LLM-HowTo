# 🧠 Lightweight RAG Pipeline Demo (LangChain + Gemini)

This project demonstrates a simple **Retrieval-Augmented Generation (RAG)** pipeline using **LangChain**, **Chroma vector database**, and **Google's Gemini LLM**.

It loads a PDF, embeds its content, stores the vectors, and answers user questions by combining document context with a language model.

---

## 🚀 Getting Started

Clone or download the repository, then run the following:

```python
# Step 1: Create a Chroma DB from the PDF in the "data" folder
vector_store = embed_and_store(
    file_path=os.path.join("data"),
    embedding_model="models/text-embedding-004",
)

# Step 2: Initialize the LLM that will answer user queries
llm = LLM_Model(
    model_name="gemini-2.0-flash",
    model_provider="google_genai",
    temperature=0,
    max_output_tokens=None,
)

# Step 3: Combine everything into a RAG system
rag_pipeline = RAG(
    vector_store=vector_store,
    llm=llm,
)

# Step 4: Ask your question
answer = my_rag.ask("What is the position of France on internal market?")
print("\nAnswer: ", answer)
```

## 🔍 How It Works

1. **Load PDF** into LangChain documents
2. **Split** the documents into overlapping chunks
3. **Embed** each chunk into high-dimensional vectors
4. **Store** those vectors in a Chroma vector database

### At query time:

- The question is embedded and compared to stored vectors using cosine similarity
- Top `k` relevant chunks are retrieved
- A prompt is built with both the retrieved content and the question
- The prompt is sent to a Gemini model (or other LLM)
- The model returns a concise answer

---

## 🔧 Future Work

This demo runs linearly for simplicity. Future improvements include:

- [ ] Persistent and editable Chroma DB (CRUD support)
- [ ] Allow for metadata configuration
- [ ] Source attribution in answers
- [ ] Customizable prompt templates
- [ ] Follow-up and conversational context
- [ ] Chatbot interface (CLI or web UI)

---

## 🧪 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Chroma DB](https://www.trychroma.com/)
- [Google Gemini](https://ai.google.dev/)
- Python 3.10+

---
