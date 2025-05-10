from pipelines.main_pipeline import run_pipeline

query = "northeastern toronto co-op eligibility"
final_output = run_pipeline(query)

print("\n🎯 FINAL RESPONSE:\n")
print(final_output)
