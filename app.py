from flask import Flask, request
from PyPDF2 import PdfReader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
# from langchain_text_splitters import RecursiveCharacterTextSplitter
import google.generativeai as genai
from flask import jsonify
from dotenv import load_dotenv
from fileloder import fileLoder,Folder_loader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from fileprocesser import get_text_chunks
from fileprocesser import get_vactor_store
from vectorstore import vector
from vectorstore import create_index
from query import search
from pinecone import Pinecone
import pdfplumber


from flask_cors import CORS

def convert_pdf_to_text(pdf_file):
    """
    Converts a PDF file to text using pdfplumber.
    """
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()  # Extract text from each page
    return text


# from langchain_core import P_Template
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"]}})

@app.route('/',methods=['post'])
def index():
#Load Folder

    user_skills = request.form['user_skills']
    degree = request.form['degree']

    # Check if files are in the request
    if 'pdf_files' not in request.files:
        return "No file part"

    files = request.files.getlist('pdf_files')  # Get the list of files
    text = []  # To store text from each PDF

    print(len(files))
    # Process each PDF file
    results = []
    for pdf_file in files:
        print("processing pdf : " + pdf_file.filename)
        if pdf_file.filename != '':  # Only process valid files
            pdf_text = convert_pdf_to_text(pdf_file)
            text.append(pdf_text)
            print(f"Text extracted from {pdf_file.filename}")
            

    #Convert pdf in to text 
        # text=fileLoder(pdf)
        # print(text)
        
        
    #Create Embadings
        embedding=get_vactor_store(pdf_text)
        # chunks=get_text_chunks(text)
        # print(embedding)

        
    #Dimention Of Vector
        dimention = len(embedding)
        # print(dimention)
        
    #create Index if Note
        create_index(dimention)
        
        for y in range(3):
            #Store Vector in Pinecone
            vector(pdf_text)
            if(y==2):
            #Output
                result1,result2,result3,result4,result5,result6,result7=search(degree,user_skills)
                print(result1)
                print(result2)
                print(result3)
                print(result4)
                print(result5)
                print(result6)
                print(result7)
                analysis_result = {
                    "name" : result1,
                    "Degree":result2,
                    "skills":result3,
                    "matching_skills":result4,
                    "working":result6,
                    "mail":result7,
                    "matching":result5
                    
                    
                }
                
                results.append(analysis_result)
            else:
                ans1,ans2,ans3,ans4,ans5,ans6,ans7=search(degree,user_skills)
                # analysis_result = {
                #     "name" : ans1,
                #     "degree":ans2,
                #     "skills":ans3,
                #     "matching_skills":ans4,
                #     "number_Of_MAtching_Skills":ans5,
                #     "working":ans6                }
                # results.append(analysis_result)
                
        index_name = "resume"
        pc = Pinecone(api_key=os.getenv("PINECONE"))
        index = pc.Index(index_name)  
        index.delete(delete_all=True, namespace="")
        print("Deleting successfully")
        # return result1,result2,result3,result4,result5,result6
    return jsonify(results) 
        
if __name__ =='__main__':
    app.run(debug=True)


# # # def conversation(resume):
# # #     """Summarizes a resume using the Gemini API.

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
# from flask import Flask, request, jsonify
# from fileloder import Folder_loader, fileLoder
# from fileprocesser import get_vactor_store
# from vectorstore import vector, create_index
# from query import search
# from pinecone import Pinecone
# import os
# import shutil

# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import os
# import shutil

# app = Flask(__name__)

# # Enable CORS for all routes
# CORS(app)

# # Serve the index.html
# @app.route('/')
# def index():
#     return send_from_directory('Front-End', 'index.html')

# @app.route('/Front-End', methods=['POST'])
# def process_resume():
#     user_skills = request.form.get('user_skills')
#     degree = request.form.get('degree')

#     if not user_skills or not degree:
#         return jsonify({'error': 'Invalid input'}), 400

#     pdf_files = request.files.getlist('pdf_files')

#     # Ensure uploads directory exists
#     uploads_dir = 'uploads'
#     os.makedirs(uploads_dir, exist_ok=True)

#     results = {}
#     for pdf in pdf_files:
#         try:
#             # Save the uploaded pdf to a designated folder
#             pdf_path = os.path.join(uploads_dir, pdf.filename)
#             pdf.save(pdf_path)

#             # Convert pdf into text
#             text = fileLoder(pdf_path)

#             # Create embeddings
#             embedding = get_vactor_store(text)

#             # Dimension of the vector
#             dimension = len(embedding)

#             # Create index if not exists
#             create_index(dimension)

#             for y in range(3):
#                 # Store Vector in Pinecone
#                 vector(text)
#                 if y == 2:
#                     # Output search results
#                     result1, result2, result3, result4, result5, result6 = search(degree, user_skills)
#                     results.update({
#                         'result1': result1,
#                         'result2': result2,
#                         'result3': result3,
#                         'result4': result4,
#                         'result5': result5,
#                         'result6': result6
#                     })
#                     break  # Exit after the first set of results

#         except Exception as e:
#             return jsonify({'error': f'Failed to process {pdf.filename}: {str(e)}'}), 500

#     # Clean up the uploads directory
#     shutil.rmtree(uploads_dir)  # Caution: This deletes all files in the uploads directory

#     return jsonify(results), 200
# from flask import Flask, request, jsonify, send_from_directory
# from fileloder import Folder_loader, fileLoder
# from fileprocesser import get_vactor_store
# from vectorstore import vector, create_index
# from query import search
# import os
# import shutil

# app = Flask(__name__)

# # Serve the static index.html file from the Front-End directory
# @app.route('/')
# def index():
#     return send_from_directory('Front-End', 'index.html')

# # Define the POST route to process the resume files
# @app.route('/Front-End', methods=['POST'])
# def process_resume():
#     user_skills = request.form.get('user_skills')
#     degree = request.form.get('degree')

#     if not user_skills or not degree:
#         return jsonify({'error': 'Invalid input'}), 400

#     pdf_files = request.files.getlist('pdf_files')

#     # Ensure uploads directory exists
#     uploads_dir = 'uploads'
#     os.makedirs(uploads_dir, exist_ok=True)

#     results = {}
#     for pdf in pdf_files:
#         try:
#             # Save the uploaded PDF to a designated folder
#             pdf_path = os.path.join(uploads_dir, pdf.filename)
#             pdf.save(pdf_path)

#             # Convert PDF into text
#             text = fileLoder(pdf_path)

#             # Create embeddings
#             embedding = get_vactor_store(text)

#             # Dimension of the vector
#             dimension = len(embedding)

#             # Create index if not exists
#             create_index(dimension)

#             for y in range(3):
#                 # Store vector in Pinecone
#                 vector(text)
#                 if y == 2:
#                     # Output search results
#                     result1, result2, result3, result4, result5, result6 = search(degree, user_skills)
#                     results.update({
#                         'result1': result1,
#                         'result2': result2,
#                         'result3': result3,
#                         'result4': result4,
#                         'result5': result5,
#                         'result6': result6
#                     })
#                     break  # Exit after the first set of results

#         except Exception as e:
#             return jsonify({'error': f'Failed to process {pdf.filename}: {str(e)}'}), 500

#     # Clean up the uploads directory after processing
#     shutil.rmtree(uploads_dir)

#     return jsonify(results), 200

# if __name__ == '__main__':
#     app.run(debug=True)
