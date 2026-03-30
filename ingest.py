import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# Load environment variables (API Key)
load_dotenv()

DATA_PATH = "data"
DB_PATH = "vector_db"

def ingest_data():
    print(f"Loading data from {DATA_PATH}...")
    
    # Load markdown/text files
    loader = DirectoryLoader(DATA_PATH, glob="**/*.md", loader_cls=TextLoader)
    documents = loader.load()
    
    print(f"Loaded {len(documents)} documents.")
    
    # Split into chunks for better retrieval
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    
    print(f"Split into {len(chunks)} chunks.")
    
    # Initialize embeddings (using OpenAI)
    embeddings = OpenAIEmbeddings()
    
    # Create and persist the vector store
    print("Creating vector store...")
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )
    
    print(f"Vector store saved to {DB_PATH}.")

if __name__ == "__main__":
    ingest_data()
