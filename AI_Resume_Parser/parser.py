import pdfplumber
import re
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

skills_file = pd.read_csv("skills.csv", header=None)
SKILLS = skills_file[0].tolist()

def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text

def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ == "PERSON":
            return ent.text

    return ""

def extract_email(text):

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

    return emails[0] if emails else ""

def extract_phone(text):

    phones = re.findall(r'\+?\d[\d -]{8,12}\d', text)

    return phones[0] if phones else ""

def extract_skills(text):

    found = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found.append(skill)

    return list(set(found))

def parse_resume(path):

    text = extract_text(path)

    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text)
    }