import requests
from bs4 import BeautifulSoup
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ScraperNode:
    def __init__(self):
        pass

    def run(self, urls):
        documents = []
        headers = {"User-Agent": "Mozilla/5.0"}
        for url in urls:
            try:
                resp = requests.get(url, timeout=10, verify=False)
                soup = BeautifulSoup(resp.text, "html.parser")
                text = soup.get_text(separator=" ", strip=True)
                documents.append({"url": url, "content": text})
            except Exception as e:
                print(f"[ScraperNode] Failed to fetch {url}: {e}")
        return {"documents": documents}
