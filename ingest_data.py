from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import GitLoader
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

# Load Data
loader = GitLoader(
    clone_url="https://github.com/viamrobotics/docs", repo_path="repo"
)
documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
documents = text_splitter.split_documents(documents)

# Load Data to vectorstore and save in db
persist_directory = 'db'
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents, embeddings, persist_directory=persist_directory
)
vectorstore.persist()
