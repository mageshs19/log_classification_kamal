# app/summarizer.py

from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def llm_classify_and_summarize(log):
    prompt = f"""
    You are a log analysis expert.

    Analyze the log and return:

    {{
      "category": "",
      "root_cause": "",
      "impact": "",
      "fix": "",
      "severity": ""
    }}

    Log:
    {log}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content