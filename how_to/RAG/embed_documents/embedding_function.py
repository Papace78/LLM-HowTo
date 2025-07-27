from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.embeddings.embeddings import Embeddings


def return_embedding_function(
    model: str = "models/text-embedding-004",
) -> Embeddings:
    return GoogleGenerativeAIEmbeddings(model=model)
