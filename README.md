# 💼 Resume & Cover Letter Optimizer

A smart, customizable job application tool powered by OpenAI's GPT-3.5 that helps you tailor your resume bullet points and generate a high-quality cover letter for any job description.

---

## 🚀 What It Does

✅ Accepts your resume (in plain text) and a job description  
✅ Uses GPT-3.5 to rewrite your resume bullet points to match the job requirements  
✅ Generates a personalized, confident, and compelling cover letter  
✅ Allows download of the cover letter as a `.docx` Word file  
✅ Never fabricates data — only uses the information in your resume

---

## 🧰 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – lightweight web interface
- [OpenAI API](https://platform.openai.com/docs) – for natural language processing
- `dotenv` – environment variable management
- `python-docx` – to generate downloadable Word documents

---

## 📂 Project Structure

```
resume-editor/
│
├── app.py              # Streamlit application
├── resume.txt          # Your plain text resume
├── .env                # Contains your OpenAI API key
├── requirements.txt    # Python dependencies
```

---

## 🧠 How It Works

1. Loads your resume from `resume.txt`
2. Accepts a pasted job description
3. Uses GPT to:
   - Tailor your bullet points (per job role)
   - Generate a well-crafted cover letter using a custom prompt
4. Displays both outputs in the app
5. Lets you download the cover letter as a `.docx` file

---

## 📥 How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/resume-editor.git
cd resume-editor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key to a `.env` file:
```env
OPENAI_API_KEY=your_key_here
```

4. Run the app:
```bash
streamlit run app.py
```

---

## 🔐 Environment Setup

Install Python dependencies:

```bash
pip install streamlit openai python-dotenv python-docx
```

Create a `.env` file:
```bash
OPENAI_API_KEY=your_actual_openai_key
```

---

## 💡 Benefits

- Saves time tailoring applications  
- Speeds up resume + cover letter customization  
- Makes your application more relevant to each role  
- Keeps your data local and secure  
- Uses only real resume info — no fakes

---

## 🙌 Acknowledgements

- Inspired by the struggle of writing endless cover letters 😅
- Powered by [OpenAI](https://platform.openai.com/)
