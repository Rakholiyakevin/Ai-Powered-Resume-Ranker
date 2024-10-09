from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from pinecone import Pinecone 

def search(degree,user_skills):
  index_name = "resume"
  # Create the embedding using GoogleGenerativeAIEmbeddings
  embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("Google_key"))
  pinecone = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=os.getenv("PINECONE")) 
  llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.3,google_api_key=os.getenv("Google_key")) 
  pc = Pinecone(api_key=os.getenv("PINECONE"))
  index = pc.Index(index_name) 
  
# completion llm  
  qa = RetrievalQA.from_chain_type(  
    llm=llm,  
    chain_type="stuff",  
    retriever=pinecone.as_retriever()  
) 
  #Candidate Name
#   print("Name of Candidate")
  query="Give ME Name persion in document(Only name nothing else) "
  response1=qa.invoke(query)
  result1 = response1['result'].strip()
#   print("\n")
#   print(result5)


  
  
  
   
  #for degree comparesion
  degree = degree
  query=f" if it's [{degree}] background give boolian value no any other word"
  response2=qa.invoke(query)
  result2 = response2['result'].strip()
#   print("\n")
#   print(f"Degree of candidate [{degree}]:",result)
  
  
  
  
  #for skills in resume
  # skills=['html','css','ruby','java',]
  query="give me list of tchnical skills in resume as a result(give me only single word skill not else)"
  response3=qa.invoke(query)
  result3=response3['result'].strip()
#   print(result1)
  

  
  
  #for skills comparesion
  user_skills = user_skills
  skills_str = ', '.join(user_skills)
  query = f"compare resume skills with [{user_skills}] and give me the number of matching skills (give me intiger of matching only nothing else)"
  response4 = qa.invoke(query)
  result4  = response4['result'].strip()
#   print("\n")
#   print("Number of skill Maching:")
#   print(result3)
  
     #for skills comparesion
  query = f"compare resume skills with [{user_skills}] and give me the number of matching skills(like this* **HTML:** Match,*CSS:** Match"
  response5 = qa.invoke(query)
  result5  = response5['result'].strip()
#   print("\n")
#   print(result4)
  
  


  
  #for work experinece
  query ="give me experience of candate like(compnyname:xyx,position:xyz,duration:time)"
  response6 = qa.invoke(query)
  result6  = response4['result'].strip()
#   print("\n")
#   print("Work Experience:")
#   print(result6)
  
  return(result1,result2,result3,result4,result5,result6)
  
#   index.delete(delete_all=True, namespace="")
#   print("Deleting successfully")

###########################################################################################################################
# from dotenv import load_dotenv
# import os
# from langchain_pinecone import PineconeVectorStore
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import RetrievalQA
# from pinecone import Pinecone

# from dotenv import load_dotenv
# import os
# from langchain_pinecone import PineconeVectorStore
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import RetrievalQA
# from pinecone import Pinecone

# def search():
#     load_dotenv()  # Load environment variables from .env file
#     index_name = "resume"

#     # Create the embedding using GoogleGenerativeAIEmbeddings
#     embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("Google_key"))
    
#     # Initialize Pinecone Vector Store
#     pinecone_store = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=os.getenv("PINECONE"))
    
#     # Language model for QA
#     llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=1, google_api_key=os.getenv("Google_key"))
    
#     # Initialize Pinecone client
#     pc = Pinecone(api_key=os.getenv("PINECONE"))
#     index = pc.Index(index_name)

#     for y in range(2):
#         # QA Chain using retriever
#         qa = RetrievalQA.from_chain_type(
#             llm=llm,  
#             chain_type="stuff",  
#             retriever=pinecone_store.as_retriever()  
#         )

#         # Perform a search query using the vector embeddings
#         query = "Fetch resume details"  # A general query to retrieve the document text
#         response = qa.invoke(query)

#         # If the response contains 'result', process it
#         if 'result' in response:
#             document_text = response['result']  # This contains the retrieved document's text

#             print("Processing document:")

#             # 1. Extract Candidate Name
#             name_query = "Extract the candidate's name from the document."
#             name_response = qa.invoke(name_query, inputs=document_text)
#             candidate_name = name_response['result'].strip()
#             print(f"\nName of Candidate: {candidate_name}")

#             # 2. Degree Comparison
#             degree_query = "Extract the candidate's degree."
#             degree_response = qa.invoke(degree_query, inputs=document_text)
#             candidate_degree = degree_response['result'].strip()
#             print(f"Degree of Candidate: {candidate_degree}")

#             # 3. Skills Comparison
#             user_skills = ['html', 'css', 'ruby', 'java']
#             skills_query = f"Compare resume skills with [{', '.join(user_skills)}] and return matching skills."
#             skills_response = qa.invoke(skills_query, inputs=document_text)
#             matching_skills = skills_response['result'].strip()
#             print(f"Matching skills: {matching_skills}")

#             # 4. Work Experience Extraction
#             experience_query = "Extract the work experience from the document."
#             experience_response = qa.invoke(experience_query, inputs=document_text)
#             work_experience = experience_response['result'].strip()
#             print(f"Work Experience: {work_experience}")
#         else:
#             print("No documents found or unable to retrieve the result.")
#     index.delete(delete_all=True, namespace="")
#     print("Deleting successfully")
#########################################################################################################################################################
# from dotenv import load_dotenv
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from pinecone import Pinecone

# def search(embb):
#     load_dotenv()  # Load environment variables from .env file
#     index_name = "resume"

#     # Initialize Pinecone client
#     pinecone = Pinecone(api_key=os.getenv("PINECONE"))
#     index = pinecone.Index(index_name)

#     # Language model for processing documents
#     llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=os.getenv("Google_key"))

#     # Retrieve documents from Pinecone by querying the vectors
#     query = "candidate resume"  # Adjust this as per your search criteria
#     query_embedding = embb * 768  # Placeholder for a query vector (replace with actual embedding)

#     results = index.query(queries=query_embedding, top_k=1)  # Retrieve top 10 matches
#     if results and 'matches' in results:
#         for match in results['matches']:
#             document_text = match['metadata'].get('text', '')  # Assume the document's text is stored in metadata

#             print("Processing document:")

#             # 1. Extract Candidate Name
#             name_query = "Extract the candidate's name from the document."
#             name_response = llm.predict(name_query, inputs=document_text)
#             candidate_name = name_response.strip()
#             print(f"\nName of Candidate: {candidate_name}") 

#             # 2. Degree Comparison
#             degree_query = "Extract the candidate's degree."
#             degree_response = llm.predict(degree_query, inputs=document_text)
#             candidate_degree = degree_response.strip()
#             print(f"Degree of Candidate: {candidate_degree}")

#             # 3. Skills Comparison
#             user_skills = ['html', 'css', 'ruby', 'java']
#             skills_query = f"Compare resume skills with [{', '.join(user_skills)}] and return matching skills."
#             skills_response = llm.predict(skills_query, inputs=document_text)
#             matching_skills = skills_response.strip()
#             print(f"Matching skills: {matching_skills}")

#             # 4. Work Experience Extraction
#             experience_query = "Extract the work experience from the document."
#             experience_response = llm.predict(experience_query, inputs=document_text)
#             work_experience = experience_response.strip()
#             print(f"Work Experience: {work_experience}")
#     else:
#         print("No documents found.")

#     # Optionally, delete the index if needed
#     index.delete(delete_all=True, namespace="")
#     print("Deleted all data in Pinecone successfully.")

# # Call the search function
# # search()



