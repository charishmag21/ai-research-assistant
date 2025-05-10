import google.generativeai as genai
import os
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt

class GeminiSummarizer:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.prompt_template = load_prompt("prompts/summarize_prompt.txt")

    def run(self, query, documents):
        summaries = []
        for doc in documents:
            prompt = self.prompt_template.replace("{{query}}", query).replace("{{content}}", doc["content"][:6000])
            try:
                response = self.model.generate_content(prompt)
                summaries.append({
                    "source": doc["url"],
                    "summary": response.text.strip()
                })
            except Exception as e:
                print(f"[GeminiSummarizer] Error for {doc['url']}: {e}")
        return {"summaries": summaries}
