import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.prompt_loader import load_prompt

class FormatterNode:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def run(self, query: str, final_answer: str):
        prompt_template = """
You are a helpful AI assistant. Format the following synthesized answer from a search agent using clean markdown:

- Convert raw URLs to markdown clickable links.
- Add clear structure with bullets, subheadings, etc.
- Keep it readable for students asking about: {query}

Answer:
{answer}
"""
        prompt = prompt_template.format(query=query, answer=final_answer)
        try:
            response = self.model.generate_content(prompt)
            return {"formatted_answer": response.text.strip()}
        except Exception as e:
            print(f"[FormatterNode] Error: {e}")
            return {"formatted_answer": final_answer}
