import requests
import os
import fitz

def download_pdf(url: str, paper_id: str):

    os.makedirs("papers", exist_ok=True)

    path = f"papers/{paper_id}.pdf"

    r = requests.get(url)

    with open(path, "wb") as f:
        f.write(r.content)

    return path

def extract_pdf_text(pdf_path: str):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text