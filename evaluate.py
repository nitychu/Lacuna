"""
Lacuna — evaluation.
Runs the analyzer on the RTI policy and compares each verdict to the
manual review. Usage: python evaluate.py        (current engine)
                      python evaluate.py old    (original engine)
"""
import sys
import analyze

ANSWER_KEY = {
    "A.5.1": "partial", "A.5.7": "partial", "A.5.10": "partial",
    "A.5.15": "covered", "A.5.17": "partial", "A.5.23": "partial",
    "A.5.24": "covered", "A.6.3": "covered", "A.7.2": "covered",
    "A.8.2": "partial", "A.8.5": "partial", "A.8.8": "covered",
    "A.8.12": "partial", "A.8.13": "partial", "A.8.16": "covered",
    "A.8.24": "partial",
}

if len(sys.argv) > 1 and sys.argv[1] == "old":
    import engine_old
    analyze.chunk_text = engine_old.chunk_text
    analyze.embed = engine_old.embed
    analyze.retrieve = engine_old.retrieve
    label = "ORIGINAL ENGINE"
else:
    label = "CURRENT ENGINE"

policy = open("rti_policy.txt").read()
results = analyze.analyze(policy)

matches = 0
counts = {"covered": 0, "partial": 0, "gap": 0, "error": 0}
print(f"\n{label}\n")
print(f"{'Control':8} {'Tool':8} {'Review':8}")
for r in results:
    tool = r["status"]
    review = ANSWER_KEY.get(r["control_id"], "?")
    counts[tool] = counts.get(tool, 0) + 1
    ok = tool == review
    matches += ok
    print(f"{r['control_id']:8} {tool:8} {review:8} {'' if ok else '<-- miss'}")

print(f"\nTool counts: {counts['covered']} covered, {counts['partial']} partial, {counts['gap']} gap")
print(f"Agreement with manual review: {matches}/{len(results)}\n")
