import os
from langchain_chroma import Chroma

from how_to.RAG.embed_documents.load_documents import LoadSplitter
from how_to.RAG.embed_documents.embedding_function import return_embedding_function
from how_to.RAG.embed_documents.vector_store_db import return_vector_store_db

DEFAULT_FILE_PATH = os.path.join("..", "data")
PERSIST_DIR = "chroma_db"


def embed_and_store(
    file_path: str = DEFAULT_FILE_PATH,
    embedding_model: str = "models/text-embedding-004",
) -> Chroma:
    """Load, embed, and store documents in a Chroma vector DB."""
    documents = LoadSplitter.transform(file_path)
    embedding_fn = return_embedding_function(embedding_model)

    vector_store = return_vector_store_db(
        embedding_function=embedding_fn,
        persist_directory=PERSIST_DIR,
    )

    document_ids = vector_store.add_documents(documents=documents)
    print(f"✅ Added {len(document_ids)} documents to the vector store.")

    return vector_store
