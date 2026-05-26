# resume_opt
resume_opt is a smart AI assistant that helps you create the perfect resume in seconds. Just input the job description and your current resume — it will instantly generate a customized, highly targeted resume tailored for that role.

# Key Features

- **Multi-Version Resume Generation**  
  Generate **3 tailored resumes** with different emphases in one click.

- **Interview Question Predictor**  
  Automatically generate the **10-15 most likely interview questions** based on the job description and your optimized resume, along with suggested thinking frameworks and key points for answering them.

- **Multiple Export Formats**  
  Export your resumes and supporting documents in various formats, including **PDF, Markdown, Word**.

- **Support multiple languages**
  As of now, **zh** and **en** are supported.

# Backend MVP

The first backend version is a local/personal FastAPI service. It supports pasted text input only and returns the optimized result synchronously.

## Run locally

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -e .
copy .env.example .env
```

Fill `DEEPSEEK_API_KEY` in `backend/.env`, then start the API:

```bash
uvicorn app.app:app --reload
```

Main endpoint:

```text
POST /api/jobs/optimize
```

Request fields:

- `job_description`: target JD text
- `resume_text`: current resume text
- `language`: `zh` or `en`
- `user_id`: optional metadata, not used for auth in the MVP
