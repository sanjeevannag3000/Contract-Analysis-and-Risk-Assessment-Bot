import PyPDF2
from docx import Document

def extract_text(file_path, file_type):
    if file_type == 'pdf':
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''.join([page.extract_text() for page in reader.pages])
    elif file_type == 'docx':
        doc = Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
    elif file_type == 'txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    return text