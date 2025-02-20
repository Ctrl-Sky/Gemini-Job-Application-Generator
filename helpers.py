from docx import Document
from datetime import datetime

def formatted_text_to_docx(formatted_text, company_name, job_title):
    doc = Document()
    for line in formatted_text.split("\n"):
        doc.add_paragraph(line)
    today = datetime.today()
    doc.save(f"cover_letter.docx")