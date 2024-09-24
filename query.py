from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA 

def search():
  index_name = "resume"
  # Create the embedding using GoogleGenerativeAIEmbeddings
  embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("Google_key"))
  Pinecone = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=os.getenv("PINECONE")) 
  llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.3,google_api_key=os.getenv("Google_key")) 
  
# completion llm  
  qa = RetrievalQA.from_chain_type(  
    llm=llm,  
    chain_type="stuff",  
    retriever=Pinecone.as_retriever()  
) 
  #Candidate Name
  print("Name of Candidate")
  query="Give ME Candidate Name(Only name nothing else) "
  response=qa.invoke(query)
  result5 = response['result'].strip()
  print("\n")
  print(result5)
  
  
  
   
  #for degree comparesion
  degree = "computer Science"
  query=f" if it's [{degree}] background give boolian value no any other word"
  response=qa.invoke(query)
  result = response['result'].strip()
  print("\n")
  print(f"Degree of candidate [{degree}]:",result)
  
  
  
  
#   #for skills in resume
#   skills=['html','css','ruby','java',]
#   query="give me list of tchnical skills in resume as a result(give me only single word skill not else)"
#   response1=qa.invoke(query)
#   result1=response1['result'].strip()
#   print(result1)
  
  
  
  
  #for skills comparesion
  user_skills = ['html', 'css', 'ruby', 'java']
  skills_str = ', '.join(user_skills)
  query = f"compare resume skills with [{user_skills}] and give me the number of matching skills (give me intiger of matching only nothing else)"
  response3 = qa.invoke(query)
  result3  = response3['result'].strip()
  print("\n")
  print("Number of skill Maching:")
  print(result3)
  
  
  
  
  #for skills comparesion
  query = f"compare resume skills with [{user_skills}] and give me the number of matching skills(like this* **HTML:** Match,*CSS:** Match"
  response4 = qa.invoke(query)
  result4  = response4['result'].strip()
  print("\n")
  print(result4)
  
  
  #for work experinece
  query ="give me experience of candate like(compnyname:xyx,position:xyz,duration:time)"
  response4 = qa.invoke(query)
  result4  = response4['result'].strip()
  print("\n")
  print("Work Experience:")
  print(result4)