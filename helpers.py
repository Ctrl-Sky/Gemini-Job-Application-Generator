from docx import Document
from datetime import datetime

def formatted_text_to_docx(formatted_text, path):
    doc = Document()
    for line in formatted_text.split("\n"):
        doc.add_paragraph(line)
    doc.save(path)