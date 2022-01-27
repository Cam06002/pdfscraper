import pdfplumber
import pyperclip as pc
from regex import Contact



with pdfplumber.open("resume.pdf") as pdf:
    page = str(pdf.pages[0].extract_text())


a1 = page
a2 = pc.copy(a1)

Contact()
