from openai import OpenAI
from textblob import TextBlob
from prompts import TECH_PROMPT
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def generate_technical_questions(tech_stack):

    prompt = f"""
You are a technical interviewer.

Generate ONLY 3 to 5 concise interview questions.

Strict rules:
- Ask questions ONLY about: {tech_stack}
- Do NOT include related frameworks unless explicitly mentioned
- Keep questions short
- Number them
- No explanations
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


def sentiment(text):
    return TextBlob(text).sentiment.polarity
