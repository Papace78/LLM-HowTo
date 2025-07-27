import os
from typing import List

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class LoadSplitter:
    """Utility class to load PDFs and split them into smaller text chunks."""

    @classmethod
    def transform(cls, file_path: str) -> List[Document]:
        """Load and split PDF documents into chunks."""
        loaded_documents = cls._load_pdf_into_documents(file_path)
        return cls._split_documents_into_chunks(loaded_documents)

    @staticmethod
    def _load_pdf_into_documents(file_path: str) -> List[Document]:
        """Load PDF files from the specified directory as LangChain documents."""
        loader = DirectoryLoader(
            path=file_path,
            glob="*.pdf",
            loader_cls=PyPDFLoader,
            show_progress=True,
        )
        documents = loader.load()
        print(f"\n✅ PDF loaded - {len(documents)} pages.")
        return documents

    @staticmethod
    def _split_documents_into_chunks(
        documents: List[Document],
        chunk_size: int = 2000,
        chunk_overlap: int = 400,
    ) -> List[Document]:
        """Split documents into smaller overlapping chunks for embedding."""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            add_start_index=True,
        )
        chunks = splitter.split_documents(documents)
        print(f"\n✅ PDF split into {len(chunks)} sub-documents.")
        return chunks
