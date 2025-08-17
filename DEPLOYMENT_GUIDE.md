🌐 TDS Project 2 Data Analyst – Render Deployment Guide

Easily deploy your AI-powered Data Analyst Agent to Render in minutes.
Follow these steps and your app will be live with a public URL.

✅ What’s Already Set Up

Your repo already includes the necessary config files:

File	Purpose
.env	Stores environment variables (e.g., API keys)
requirements.txt	Python dependencies
Procfile	Tells Render how to start the app (Gunicorn)
runtime.txt	Python version specification
.gitignore	Prevents committing sensitive files like .env
🔑 1. Configure Environment Variables

Create a .env file in your project root (for local testing):

# Google Gemini API Keys (copy one key into all slots if you have only one)
gemini_api_1=your_api_key_here
gemini_api_2=your_api_key_here
gemini_api_3=your_api_key_here
gemini_api_4=your_api_key_here
gemini_api_5=your_api_key_here
gemini_api_6=your_api_key_here
gemini_api_7=your_api_key_here
gemini_api_8=your_api_key_here
gemini_api_9=your_api_key_here
gemini_api_10=your_api_key_here
LLM_TIMEOUT_SECONDS=240


⚠️ Never commit your .env file to GitHub. Keep it local and add to .gitignore.

📤 2. Push Code to GitHub
cd /path/to/project
git init
git add .
git commit -m "Initial commit with Render deployment config"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main

🚀 3. Deploy to Render

Go to render.com → Sign in with GitHub.

Click New → Web Service.

Select your GitHub repo.

Fill in deployment settings:

Environment → Python 3.x

Build Command →

pip install -r requirements.txt


Start Command (example for FastAPI):

gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT


(replace app:app with your actual entrypoint if different, e.g. main:app)

Click Create Web Service → Render will build and deploy.

After a few minutes, you’ll get a live public URL (e.g., https://your-service.onrender.com).

🌍 4. Add Environment Variables in Render

Go to your Render service → Settings → Environment → Environment Variables.

Add your Gemini keys and other variables just like in .env.

Example:

Key	Value
gemini_api_1	your_api_key_here
…	…
LLM_TIMEOUT_SECONDS	240
🧪 5. Test Locally
source venv/bin/activate   # Windows: venv\Scripts\activate
uvicorn app:app --host 0.0.0.0 --port 8000


Visit: http://localhost:8000

⚙ Environment Variable Reference
Variable	Description	Default	Required
gemini_api_1……gemini_api_10	Google Gemini API keys	—	✅ (at least 1; if only one, duplicate it in all slots)
LLM_TIMEOUT_SECONDS	LLM Max Time for task	240	❌
PORT	App port	Auto-assigned by Render	✅ (use $PORT)
🛠 Troubleshooting

Common Issues

Module not found → Check requirements.txt.

Port errors → Always bind to $PORT (Render assigns it).

API key errors → Make sure all keys are added in Render Environment Variables.

Build fails → Check Render Logs for dependency errors.

View Logs:

Go to your service → Logs tab.

📚 Helpful Links

📖 Render Docs

🤖 Google AI Docs

⚡ With this setup, your Data Analyst Agent will run reliably on Render and scale automatically with traffic.
