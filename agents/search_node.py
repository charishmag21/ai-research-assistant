import os
import requests
from dotenv import load_dotenv

class SearchNode:
    def __init__(self, max_results: int = 5):
        load_dotenv()
        self.api_key = os.getenv("SERPER_API_KEY")
        self.max_results = max_results

    def run(self, query: str):
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {"q": query}
        try:
            response = requests.post("https://google.serper.dev/search", json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            urls = [item["link"] for item in data.get("organic", [])[:self.max_results]]
            return {"urls": urls}
        except Exception as e:
            print(f"[SearchNode] Search failed: {e}")
            return {"urls": []}
