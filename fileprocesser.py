from fileloder import fileLoder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import google.generativeai as genai
import os
load_dotenv()
genai.configure(api_key = os.getenv("Google_key"))

def get_text_chunks(text):
    
    text_splitters = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitters.split_text(text)
    # print(chunks)
    return(chunks)
def get_vactor_store(chunks):
    load_dotenv()
    genai.configure(api_key = os.getenv("Google_key"))
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=os.getenv("Google_key"))
    vector = embeddings.embed_query(chunks)
    
    return(vector)

    

    