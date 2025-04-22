import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from io import BytesIO
from docx import Document
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Load resume
with open("resume.txt", "r") as file:
    resume_text = file.read()

# Function to export text as a Word file
def generate_word_file(text, filename):
    doc = Document()
    doc.add_paragraph(text)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# Streamlit UI
st.title("💼 Resume & Cover Letter Optimizer")
st.write("Paste a job description below and let the app tailor your resume bullet points and generate a custom cover letter.")

job_description = st.text_area("🔍 Job Description", height=250)

if st.button("✨ Optimize My Resume & Create Cover Letter"):
    if not job_description.strip():
        st.warning("Please paste a job description before proceeding.")
    else:
        with st.spinner("Crafting your custom application package..."):
            # Prompt to tailor resume bullet points
            resume_prompt = f"""
            You are a professional resume editor.
            Here's my resume:
            {resume_text}

            Here's the job description:
            {job_description}

            Edit the bullet points from my resume to better align with the job description.
            Do NOT invent information. Use only what’s in the resume. Keep bullet points grouped under each job title/role exactly as they are in the original resume.
            Do not rewrite into a paragraph — keep it as organized, impactful bullet points.
            Make it confident, compelling, and job-specific.
            """

            try:
                resume_response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": resume_prompt}],
                    temperature=0.7
                )

                edited_bullets = resume_response.choices[0].message.content

                st.subheader("📌 Tailored Resume Bullet Points")
                st.text_area("Your Updated Bullet Points", edited_bullets, height=300)

                # Prompt to generate cover letter
                cover_letter_prompt = f"""
                You are a professional cover letter writer.
                My resume:
                {resume_text}

                Job description:
                {job_description}

                Write a cover letter for me for this job description, showing that I have all the skills required for this job. Use the company's name in the cover letter. Stay away from cliches—make the email interesting and great to read so that I stand out in the reader's mind. Make it seem like if they don't hire me, it will be a mistake. Also mention that if there is any skill that the job requires and I don't have it—it's just a skill, it takes me less than a week to acquire new tech skills—I am a straight A student, with excellent academic record and I am the person at work that managers and senior managers "trust" with everything—see my LinkedIn recommendations from my ex managers. Do not invent any figures or information, use only the information given in the resume. I am a great team player and my best comes out at work. I was so good where I interned, they hired me as soon as my internship was done, I had made a place in the team. So write an amazing cover letter. Source all quantitative claims from resume, do not invent anything.
                """

                cover_letter_response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": cover_letter_prompt}],
                    temperature=0.7
                )

                cover_letter = cover_letter_response.choices[0].message.content

                st.subheader("📄 Custom Cover Letter")
                st.text_area("Your Cover Letter", cover_letter, height=400)

                # Download as Word
                cover_letter_file = generate_word_file(cover_letter, "cover_letter.docx")
                st.download_button(
                    label="📥 Download Cover Letter as .docx",
                    data=cover_letter_file,
                    file_name="Cover_Letter.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
