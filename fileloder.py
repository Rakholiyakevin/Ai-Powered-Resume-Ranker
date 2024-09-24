import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
def Folder_loder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print(file_path,filename)
        
def fileLoder(file_path):
    path =file_path
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
# page = reader.pages[0]
    for i in range(number_of_pages):
        page = reader.pages[i]
    text = page.extract_text()
    return(text)




# def conversation(resume):
#     Prompt = ". What is this candidate's professional experience? Can you summarize their roles and responsibilities at each job listed here?  Have they completed any notable projects during their work experience? If so, what were those projects and what was their contribution?  In their skills section, can you determine whether they possess any hard skills required for our open position? How proficient are they in each skill based on self-assessment or endorsements? From Given :{resume}"
#     model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3,google_api_key="Google_key")
#     Prompt_Template = PromptTemplate(template=Prompt,input_variables=['resume'])
#     chain = Prompt_Template|model
#     chain.invoke(resume)
    