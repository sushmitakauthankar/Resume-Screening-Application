from docx import Document
import io
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader

def read(file):
    filename = secure_filename(file.filename)
    file_ext = filename.rsplit('.', 1)[-1].lower()

    if file_ext in ['pdf', 'docx', 'txt']:
        file_content = file.read() 

        if file_ext == 'pdf':
            return read_pdf(file_content)  
        elif file_ext == 'docx':
            return read_docx(file_content)
        elif file_ext == 'txt':
            return read_txt(file_content) 
    else:
        raise ValueError("Unsupported file format")


def read_txt(file_content):
    try:
        # Decode the bytes to string assuming UTF-8 encoding
        text = file_content.decode('utf-8')
        return text
    except Exception as e:
        print(f"Error reading TXT file: {str(e)}")
        return None


def read_pdf(file_content):
    try:
        reader = PdfReader(io.BytesIO(file_content))
        text = []
        num_pages = len(reader.pages)
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
            else:
                print(f"Warning: No text extracted from page {page_num}")
        
        return "\n".join(text)
    except Exception as e:
        print(f"Error reading PDF file: {str(e)}")
        return None


def read_docx(file_content):
    document = Document(io.BytesIO(file_content))
    text = []
    for paragraph in document.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)
