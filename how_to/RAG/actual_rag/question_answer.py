import os

from langchain import hub
from langchain_core.documents import Document
from langchain_chroma import Chroma

from how_to.RAG.embed_documents.embed_documents import embed_and_store
from how_to.RAG.prompt_LLM.prompt_LLM import LLM_Model

QUERY = "Summarize the discussion on agricultural policy."


class RAG:
    def __init__(self, vector_store: Chroma, llm: LLM_Model):
        """Initialize RAG with vector store and LLM."""
        self.vector_store = vector_store
        self.llm = llm

    def ask(self, query: str, show_prompt: bool = False) -> str:
        """Query the RAG pipeline and return an answer."""
        context = self._retrieve_documents(query, k=6)
        prompt = self._build_prompt(context, query)

        if show_prompt:
            print("\nPrompt:\n", prompt)

        return self.llm.prompt(human_message=prompt)

    def _retrieve_documents(self, query: str, k: int) -> str:
        """Retrieve top-k relevant documents as context."""
        results = self.vector_store.similarity_search(query, k=k)
        return "\n\n".join(doc.page_content for doc in results)

    @staticmethod
    def _build_prompt(context: str, query: str) -> str:
        """Build a prompt using LangChain Hub template."""
        prompt_template = hub.pull("rlm/rag-prompt")
        return prompt_template.invoke({"context": context, "question": query}).to_string()


if __name__ == "__main__":
    # Embed and store documents
    vector_store = embed_and_store(
        file_path=os.path.join("data"),
        embedding_model="models/text-embedding-004",
    )

    # Initialize the LLM
    llm = LLM_Model(
        model_name="gemini-2.0-flash",
        model_provider="google_genai",
        temperature=0,
        max_output_tokens=None,
    )

    # Run the full RAG pipeline
    rag_pipeline = RAG(vector_store=vector_store, llm=llm)

    result = rag_pipeline.ask("What is the position of France on internal market?")
    print("\nAnswer:", result)
