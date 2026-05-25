from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
import io

def criar_documento():
    pdf_buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    return doc, pdf_buffer

