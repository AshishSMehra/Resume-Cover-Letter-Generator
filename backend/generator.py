from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model_name="gpt-4", openai_api_key="your-api-key")

def generate_resume(name, job_desc, similar_resumes):
    prompt = f"Generate a professional resume for {name} applying for:\n{job_desc}\n\nReference these resumes:\n{similar_resumes}"
    return llm.predict(prompt)

def generate_cover_letter(name, job_desc, similar_resumes):
    prompt = f"Write a tailored cover letter for {name} based on:\n{job_desc}\n\nReference resumes:\n{similar_resumes}"
    return llm.predict(prompt)
