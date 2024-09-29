# from PyPDF2 import PdfReader
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
# from langchain_text_splitters import RecursiveCharacterTextSplitter
import google.generativeai as genai

from dotenv import load_dotenv
from fileloder import fileLoder,Folder_loader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from fileprocesser import get_text_chunks
from fileprocesser import get_vactor_store
from vectorstore import vector
from vectorstore import create_index
from query import search
# from langchain_core import P_Template

#Load Folder
path="./pdfs"

pdf_files = Folder_loader(path)
for pdf in pdf_files:

#Convert pdf in to text 
    text=fileLoder(pdf)
    print(text)
    
#Create Embadings
    embedding=get_vactor_store(text)
    print(embedding)

    
#Dimention Of Vector
    dimention = len(embedding)
    print(dimention)
    
#create Index if Note
    create_index(dimention)
    
#Store Vector in Pinecone
    vector(text)
    
#Output
search()
    
    











    

# def conversation(resume):
#     """Summarizes a resume using the Gemini API.

#     Args:
#         resume (str): Text content of the resume.

#     Returns:
#         str: Summary of the resume's key points (experience, skills, etc.).
#     """
#     Prompt = """"What is this candidate's professional experience? Can you summarize their roles and responsibilities at each job listed here? 
#         Have they completed any notable projects during their work experience? If so, what were those projects and what was their contribution? 
#         In their skills section, can you determine whether they possess any hard skills required for our open position? How proficient are they in each skill based on self-assessment or endorsements?(The cleaned and formatted text) From Given :{resume}"""
    
    # model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3,google_api_key=os.getenv("Google_key"))
#     Prompt_Template = PromptTemplate(template=Prompt,input_variables=['resume'])
#     chain = Prompt_Template|model
#     chat=chain.invoke(resume)
#     print(chat)
    
    
# conversation(resume)