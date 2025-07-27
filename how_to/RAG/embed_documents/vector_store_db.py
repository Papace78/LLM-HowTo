import os

from langchain_chroma import Chroma
from langchain_core.embeddings.embeddings import Embeddings

from how_to.RAG.embed_documents.embedding_function import return_embedding_function


def return_vector_store_db(
    embedding_function: Embeddings,
    persist_directory: str,
) -> Chroma:
    return Chroma(
        collection_name="verbatim_report",
        embedding_function=embedding_function,
        persist_directory=persist_directory,
    )
