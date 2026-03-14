import streamlit as st
import pdfplumber
from skills import skills_list

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

def extract_text(pdf):
    text = ""
    with pdfplumber.open(pdf) as pdf_file:
        for page in pdf_file.pages:
            text += page.extract_text()
    return text.lower()

def extract_skills(text):
    detected = []
    for skill in skills_list:
        if skill in text:
            detected.append(skill)
    return detected

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    st.subheader("Detected Skills")
    st.write(skills)

    score = len(skills) * 10

    st.subheader("Resume Score")
    st.write(str(score) + "%")
