from fastapi import FastAPI, UploadFile, File, Form
from embeddings import generate_embeddings
from generator import generate_resume, generate_cover_letter
from parser import extract_text_from_pdf
from vector_store import store_resume_embedding, search_similar_resumes

app = FastAPI()

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_text_from_pdf(await file.read())
    vector = generate_embeddings(text)
    store_resume_embedding(file.filename, vector, text)
    return {"message": "Resume uploaded successfully"}

@app.post("/generate/")
async def generate_documents(name: str = Form(...), job_description: str = Form(...)):
    similar_resumes = search_similar_resumes(job_description)
    resume = generate_resume(name, job_description, similar_resumes)
    cover_letter = generate_cover_letter(name, job_description, similar_resumes)
    return {"resume": resume, "cover_letter": cover_letter}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
