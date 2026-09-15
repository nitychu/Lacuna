"""
Lacuna — gap analysis.
For each framework control, retrieve the most relevant policy chunks,
then have the LLM judge whether the policy covers the control.
"""
import json
import anthropic
from engine import chunk_text, embed, retrieve

client = anthropic.Anthropic()

JUDGE_PROMPT = """You are a GRC analyst assessing whether an organization's \
written policies address a specific security control.

CONTROL:
{control_id} — {control_title}
{control_text}

RELEVANT POLICY EXCERPTS (retrieved by semantic search):
{excerpts}

Judge how well the policy addresses this control. Respond in strict JSON:
{{"status": "covered" | "partial" | "gap",
  "rationale": "one or two sentences citing what the policy does or does not say",
  "evidence": "the single most relevant phrase from the excerpts, or null if none"}}

- "covered": the policy clearly addresses the control's intent.
- "partial": the policy touches it but is incomplete or vague.
- "gap": nothing in the excerpts addresses this control.
Respond with ONLY the JSON, no other text."""


def analyze(policy_text, controls_path="controls_iso27001.json"):
    data = json.load(open(controls_path))
    controls = data["controls"]

    chunks = chunk_text(policy_text)
    chunk_vecs = embed(chunks)

    results = []
    for ctrl in controls:
        hits = retrieve(ctrl["text"], chunks, chunk_vecs)
        excerpts = "\n".join("- " + h["chunk"] for h in hits) or "(none)"
        prompt = JUDGE_PROMPT.format(
            control_id=ctrl["id"], control_title=ctrl["title"],
            control_text=ctrl["text"], excerpts=excerpts)
        msg = client.messages.create(
            model="claude-sonnet-4-5", max_tokens=300,
            messages=[{"role": "user", "content": prompt}])
        raw = msg.content[0].text.strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
            raw = raw.strip()
        try:
            verdict = json.loads(raw)
        except json.JSONDecodeError:
            verdict = {"status": "error", "rationale": raw[:120], "evidence": None}
        verdict["control_id"] = ctrl["id"]
        verdict["control_title"] = ctrl["title"]
        results.append(verdict)
    return results


if __name__ == "__main__":
    sample = """INFORMATION SECURITY POLICY
All administrator accounts require multi-factor authentication.
User access is reviewed quarterly by the security team.
Backups are performed nightly and stored in a separate region.
All employees complete security awareness training annually.
Passwords must be at least 12 characters and rotated every 90 days."""
    out = analyze(sample)
    for r in out:
        print(f"[{r['status'].upper():8}] {r['control_id']} {r['control_title']}")
