from agents.search_node import SearchNode
from agents.scraper_node import ScraperNode
from agents.gemini_node import GeminiSummarizer
from agents.synthesis_node import SynthesisAgent
from agents.formatter_node import FormatterNode
from agents.enhancer_node import EnhancerNode
from utils.query_cache import check_cache, save_to_cache


def run_pipeline(query: str) -> str:
    print(f"🔍 Running pipeline for: {query}")

    cached = check_cache(query)
    if cached:
        print("⚡ Found in cache. Skipping full pipeline.")
        return cached
    
    # 1. Search
    search = SearchNode()
    search_output = search.run(query)
    urls = search_output["urls"]

    # 2. Scrape
    scraper = ScraperNode()
    scraped_output = scraper.run(urls)
    documents = scraped_output["documents"]

    # 3. Summarize
    summarizer = GeminiSummarizer()
    summary_output = summarizer.run(query, documents)
    summaries = summary_output["summaries"]

    # 4. Synthesize
    synthesizer = SynthesisAgent()
    final = synthesizer.run(query, summaries)
    final_answer = final["final_answer"]

    # 5. Format
    formatter = FormatterNode()
    formatted = formatter.run(query, final_answer)["formatted_answer"]

    # 6. Enhance (optional polishing)
    enhancer = EnhancerNode()
    polished = enhancer.run(query, formatted)["enhanced_answer"]

    save_to_cache(query, polished)
    return polished
