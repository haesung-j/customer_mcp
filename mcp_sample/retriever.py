import os
import warnings
from dotenv import load_dotenv
from pathlib import Path

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

BASE_DIR = Path(__file__).parents[1]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


warnings.filterwarnings("ignore")


DATA_PATH = BASE_DIR / "mcp_sample" / "data"
DB_PATH = BASE_DIR / "mcp_sample" / "vector_store"
PERSISTANT_DIRECTORY = DB_PATH

os.makedirs(PERSISTANT_DIRECTORY, exist_ok=True)


def get_retriever():
    loader = PyMuPDFLoader(DATA_PATH / "ai_brief.pdf")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)

    documents = loader.load()
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    if os.path.exists(PERSISTANT_DIRECTORY) and any(os.listdir(PERSISTANT_DIRECTORY)):
        print(f"Loading existing vector store: {PERSISTANT_DIRECTORY}")
        vector_store = Chroma(
            persist_directory=str(PERSISTANT_DIRECTORY),
            embedding_function=embeddings,
            collection_name="ai_trends",
        )
    else:
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            collection_name="ai_trends",
            persist_directory=str(PERSISTANT_DIRECTORY),
        )

    return vector_store.as_retriever(search_kwargs={"k": 3})


def format_docs(docs):
    result = []
    for i, doc in enumerate(docs):
        res = f"### 결과 {i+1}. Page : {doc.metadata['page']+1}\n"
        res += doc.page_content
        result.append(res)
    return "\n\n=========================\n\n".join(result)
