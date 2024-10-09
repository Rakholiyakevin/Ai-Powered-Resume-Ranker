# from dotenv import load_dotenv
# import os
# # import pinecone
# from langchain_pinecone import PineconeVectorStore
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.docstore.document import Document
# from langchain.chains import RetrievalQA
# from fileprocesser import get_vactor_store
# from pinecone import Pinecone, ServerlessSpec 

# def CreateIndex():
#     index_name= "resume"
#     pc = Pinecone(api_key=os.getenv("PINECONE"))
#       # Create the index with the correct syntax
#     s=ServerlessSpec(
#         cloud="aws",
#         region="us-east-1"
#     ) 

#       # Check if the index already exists
#     if index_name not in pc.list_indexes():
#         # Create the index if it doesn't exist
#         pc.create_index(
#             name=index_name,
#             dimension=873,
#             metric="cosine",
#             spec=s
#         )
  
# def vector(text):
#   index_name= "resume"
#   pc = Pinecone(api_key=os.getenv("PINECONE"))
#   # Create the embedding using GoogleGenerativeAIEmbeddings
#   embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("Google_key"))
#   vectors = embeddings.embed_query(text)
#   documents = [Document(page_content=text)]
  
#   #Initialize PineconeVectorStore with the embedding
#   pinecone = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=os.getenv("PINECONE"))
#   # Create the index with the correct syntax
#   pinecone.add_documents(documents)

#   print("data store in vector successfully stored")
from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec 
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.docstore.document import Document

def create_index(Dimention):
    
    pc = Pinecone(api_key=os.getenv("PINECONE"))
    index_name = "resume"
    # existing_indexes = pc.list_indexes().names()

    # Create the index with the correct dimension
    vector_dimension = Dimention   # Update this to match the embedding dimension

    s = ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )

    # Check if the index already exists
    if index_name not in pc.list_indexes().names():
        # Create the index if it doesn't exist
        pc.create_index(
            name=index_name,
            dimension=vector_dimension,  # Use the correct dimension here
            metric="cosine",
            spec=s
        )
        print("Index created successfully")
    else:
        print("Index already exists")

def vector(text):

    index_name = "resume"#name of index
    pc = Pinecone(api_key=os.getenv("PINECONE"))
    


    
    # Create the embedding using GoogleGenerativeAIEmbeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("Google_key"))
    vectors = embeddings.embed_query(text)
    documents = [Document(page_content=text)] #Convert into Document
   
    # Initialize PineconeVectorStore with the embedding
    pinecone_store = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=os.getenv("PINECONE"))
    for i in range(5):
    # Add documents to Pinecone
        pinecone_store.add_documents(documents)

    print("Data successfully stored in vector store")
