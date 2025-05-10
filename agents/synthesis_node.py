class SynthesisAgent:
    def __init__(self):
        pass

    def run(self, query, summaries):
        combined_sections = []
        for s in summaries:
            section = f"🔗 **Source:** <{s['source']}>\n📝 {s['summary']}"
            combined_sections.append(section)

        combined = "\n\n".join(combined_sections)

        final_answer = f"""📌 **Summary for:** _{query}_

Here’s what we found across {len(summaries)} sources:

{combined}

👉 For official confirmation, contact your academic advisor or co-op coordinator.
"""
        return {"final_answer": final_answer}
