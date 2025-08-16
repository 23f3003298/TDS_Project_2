import os
import json
import google.generativeai as genai

# Configure Gemini with API key
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise ValueError("GENAI_API_KEY environment variable is not set.")
genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

SYSTEM_PROMPT = """
You are a data extraction and analysis assistant.  
Your job is to:
1. Write Python code that scrapes the relevant data needed to answer the user's query. 
   - If no URLs are given, check the "uploads" folder and read provided files, then generate metadata.
2. List all Python libraries required.
3. Identify and output the main questions the user is asking.

Respond ONLY in valid JSON:
{
  "code": "...",
  "libraries": ["..."],
  "questions": ["..."]
}
"""

def parse_question_with_llm(question_text, uploaded_files=None, urls=None, folder="uploads"):
    uploaded_files = uploaded_files or []
    urls = urls or []

    user_prompt = f"""
Question:
"{question_text}"

Uploaded files:
"{uploaded_files}"

URLs:
"{urls}"

Your task is to generate Python 3 code that loads/scrapes data. 
Follow the rules:
- Save the dataset as {folder}/data.csv.
- Save metadata (df.info, df.head, etc.) to {folder}/metadata.txt.
- Create the folder if it doesn’t exist.
- Use only standard libs + pandas, numpy, bs4, requests.
- Don’t solve the question, only scrape + collect metadata.
"""

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(
        [SYSTEM_PROMPT, user_prompt],
        generation_config={"response_mime_type": "application/json"}
    )

    output = response.text or response.candidates[0].content.parts[0].text
    return json.loads(output)


SYSTEM_PROMPT2 = """
You are a data analysis assistant.  
Your job is to:
1. Write Python code to solve the questions using metadata.
2. Save results to "{folder}/result.json" or other suitable file (images as base64 PNG).
3. Return JSON with:
   - "code": "...",
   - "libraries": ["..."]
"""

def answer_with_data(question_text, folder="uploads"):
    metadata_path = os.path.join(folder, "metadata.txt")
    with open(metadata_path, "r") as file:
        metadata = file.read()

    user_prompt = f"""
Question:
{question_text}

Metadata:
{metadata}
"""

    model = genai.GenerativeModel(MODEL_NAME)
    system_prompt2 = SYSTEM_PROMPT2.format(folder=folder)

    response = model.generate_content(
        [system_prompt2, user_prompt],
        generation_config={"response_mime_type": "application/json"}
    )

    output = response.text or response.candidates[0].content.parts[0].text
    return json.loads(output)
