import fitz  # PyMuPDF
import pdfplumber
import docx
import re
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

# Function to extract text from PDF using PyMuPDF
def extract_text_pymupdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text.strip()

# Function to extract text from PDF using pdfplumber
def extract_text_pdfplumber(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n" if page.extract_text() else ""
    return text.strip()

# Function to extract text from DOCX
def extract_text_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def preprocess_text(text):
    # Remove extra spaces, newlines, and special characters
    text = re.sub(r"\s+", " ", text)  # Remove multiple spaces/newlines
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters

    # Convert to lowercase
    text = text.lower()

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = text.split()
    text = " ".join([word for word in words if word not in stop_words])

    return text.strip()

def process_resume(file_path):
    if file_path.endswith(".pdf"):
        text = extract_text_pymupdf(file_path)  # OR use extract_text_pdfplumber(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_docx(file_path)
    else:
        raise ValueError("Unsupported file format!")

    cleaned_text = preprocess_text(text)
    return cleaned_text

# Test with a sample resume
resume_text = process_resume("AshishMehra_Resume.pdf")
print(resume_text)  # Processed resume text
