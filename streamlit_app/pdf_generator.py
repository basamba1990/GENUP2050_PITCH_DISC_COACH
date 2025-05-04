
from fpdf import FPDF
from io import BytesIO

def create_pdf(transcription, profile, feedback):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "GENUP2050 - Rapport de pitch", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Profil DISC sélectionné : {profile}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, "Transcription :")
    pdf.multi_cell(0, 10, transcription)
    pdf.ln(5)
    pdf.multi_cell(0, 10, "Feedback IA :")
    pdf.multi_cell(0, 10, feedback)

    pdf_output = BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()
