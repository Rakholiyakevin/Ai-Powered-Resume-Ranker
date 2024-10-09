# # from PyPDF2 import PdfReader
# # from langchain_google_genai import GoogleGenerativeAIEmbeddings
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# import google.generativeai as genai

# from dotenv import load_dotenv
# from fileloder import fileLoder,Folder_loader
# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# from fileprocesser import get_text_chunks
# from fileprocesser import get_vactor_store
# from vectorstore import vector
# from vectorstore import create_index
# from query import search
# from pinecone import Pinecone
# # from langchain_core import P_Template

# #Load Folder
# path="./pdfs"
# user_skills = ['html', 'css', 'ruby', 'java']
# degree = "computer Science"


# pdf_files = Folder_loader(path)
# for pdf in pdf_files:

# #Convert pdf in to text 
#     text=fileLoder(pdf)
#     # print(text)
    
# #Create Embadings
#     embedding=get_vactor_store(text)
#     # chunks=get_text_chunks(text)
#     # print(embedding)

    
# #Dimention Of Vector
#     dimention = len(embedding)
#     # print(dimention)
    
# #create Index if Note
#     create_index(dimention)
    
#     for y in range(3):
#          #Store Vector in Pinecone
#         vector(text)
#         if(y==2):
#         #Output
#             result1,result2,result3,result4,result5,result6=search(degree,user_skills)
#             print(ans1)
#             print(ans2)
#             print(ans3)
#             print(ans4)
#             print(ans5)
#             print(ans6)
#         else:
#             ans1,ans2,ans3,ans4,ans5,ans6=search()
#     index_name = "resume"
#     pc = Pinecone(api_key=os.getenv("PINECONE"))
#     index = pc.Index(index_name)  
#     index.delete(delete_all=True, namespace="")
#     print("Deleting successfully")

# # def conversation(resume):
# #     """Summarizes a resume using the Gemini API.

# #     Args:
# #         resume (str): Text content of the resume.

# #     Returns:
# #         str: Summary of the resume's key points (experience, skills, etc.).
# #     """
# #     Prompt = """"What is this candidate's professional experience? Can you summarize their roles and responsibilities at each job listed here? 
# #         Have they completed any notable projects during their work experience? If so, what were those projects and what was their contribution? 
# #         In their skills section, can you determine whether they possess any hard skills required for our open position? How proficient are they in each skill based on self-assessment or endorsements?(The cleaned and formatted text) From Given :{resume}"""
    
#     # model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3,google_api_key=os.getenv("Google_key"))
# #     Prompt_Template = PromptTemplate(template=Prompt,input_variables=['resume'])
# #     chain = Prompt_Template|model
# #     chat=chain.invoke(resume)
# #     print(chat)
    
    
# # conversation(resume)
from flask import Flask, request, jsonify
from fileloder import Folder_loader, fileLoder
from fileprocesser import get_vactor_store, get_text_chunks
from vectorstore import vector, create_index
from query import search
from pinecone import Pinecone
import os

app = Flask(__name__)

@app.route('/process-resume', methods=['POST'])
def process_resume():
    data = request.get_json()
    path = data.get('path')
    user_skills = data.get('user_skills')
    degree = data.get('degree')

    if not path or not user_skills or not degree:
        return jsonify({'error': 'Invalid input'}), 400

    pdf_files = Folder_loader(path)

    for pdf in pdf_files:
        # Convert pdf into text
        text = fileLoder(pdf)

        # Create embeddings
        embedding = get_vactor_store(text)

        # Dimension of the vector
        dimension = len(embedding)

        # Create index if not exists
        create_index(dimension)

        for y in range(3):
            # Store Vector in Pinecone
            vector(text)
            if y == 2:
                # Output search results
                result1, result2, result3, result4, result5, result6 = search(degree, user_skills)
                return jsonify({
                    'result1': result1,
                    'result2': result2,
                    'result3': result3,
                    'result4': result4,
                    'result5': result5,
                    'result6': result6
                }), 200

    return jsonify({'message': 'Resume processing completed'}), 200

if __name__ == '__main__':
    app.run(debug=True)
