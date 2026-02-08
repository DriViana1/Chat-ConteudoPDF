# Responsavel por treinar o modelo e como ele funciona

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_chroma import Chroma

from huggingface_hub import login
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['HUGGING_FACE_TOKEN'] = os.getenv('HUGGING_FACE_TOKEN')
directory=r"ChatbotWebsite\chromadb"


embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = Chroma(embedding_function=embeddings_model, persist_directory=directory)


def read_pdf(pdf_file):
    pdf_page = PdfReader(pdf_file)
    
    text = ""
    for page in pdf_page.pages:
        text += page.extract_text()
        
    return text

def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs = text_splitter.split_text(text)
    docs_chunks=text_splitter.create_documents(docs)
    return docs_chunks

def create_embeddings(texts):
    
    try:
        embeddings = embeddings_model.embed_documents([doc.page_content for doc in texts])
        print("Vector Embeddings created successfully")
    except Exception as e:
        print(f"Error creating vector embeddings: {e}")

    
    return embeddings

def push_toChroma(split_text): 
    vector_store.add_documents(documents=split_text)
    
    print('Upload sucess')
    
    
def search_chroma(query):
    result = vector_store.search(query=query, search_type='similarity')
    
    return result
    
    
    

    
    