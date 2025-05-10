import os
import re
from dotenv import load_dotenv
import google.generativeai as genai

class EnhancerNode:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def run(self, query, formatted_text):
        prompt = f"""
You are an AI assistant enhancing a synthesized answer to a student’s university-related question.

Only include information that is:
- Directly related to **Northeastern University Toronto**.
- About Northeastern’s official policies, fees, co-op eligibility, or programs.
- Verified from trusted university sources.

✂️ Remove any mention of other universities or general information not specific to Northeastern Toronto.

🎯 Format the response with:
- A title (## Heading)
- Bullet points or subheadings for readability
- Clear, precise, non-redundant content
- Markdown-compatible links (e.g., [title](url))

📝 User Question: {query}

📄 Draft Answer:
{formatted_text}

Return ONLY the enhanced markdown-formatted answer.
"""

        try:
            response = self.model.generate_content(prompt)
            enhanced = response.text.strip()
        except Exception as e:
            print(f"[EnhancerNode] Gemini enhancement failed: {e}")
            enhanced = formatted_text

        # Post-processing: add emojis and clickable links
        enhanced = self._convert_links(enhanced)
        enhanced = self._add_visual_emojis(enhanced)
        return {"enhanced_answer": enhanced}

    def _convert_links(self, text: str) -> str:
        url_pattern = re.compile(r"(https?://[^\s)]+)")
        return url_pattern.sub(r"<\1>", text)

    def _add_visual_emojis(self, text: str) -> str:
        replacements = {
            "book an appointment": "📅 **Book an appointment**",
            "calendar": "📆 **Calendar**",
            "apply here": "📝 **Apply here**",
            "click here": "👉 **Click here**",
            "contact your academic advisor": "📩 **Contact your academic advisor**"
        }
        for phrase, replacement in replacements.items():
            text = re.sub(phrase, replacement, text, flags=re.IGNORECASE)
        return text
