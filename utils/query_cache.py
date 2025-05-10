import json
import os

DATA_PATH = "data/past_queries.json"

def load_cache():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_to_cache(query: str, response: str):
    cache = load_cache()
    cache[query] = response
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)

def check_cache(query: str):
    cache = load_cache()
    return cache.get(query)
