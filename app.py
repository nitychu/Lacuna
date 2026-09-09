"""Lacuna — Flask web app. Upload policy text, get a control-gap report."""
from flask import Flask, request, render_template_string
from analyze import analyze

app = Flask(__name__)

PAGE = """
<!doctype html>
<html><head><title>Lacuna</title>
<style>
  body { font-family: -apple-system, system-ui, sans-serif; max-width: 820px;
         margin: 40px auto; padding: 0 20px; color: #1a2332; line-height: 1.5; }
  h1 { letter-spacing: 1px; margin-bottom: 4px; }
  .sub { color: #667; margin-top: 0; }
  textarea { width: 100%; height: 200px; padding: 12px; font-size: 14px;
             border: 1px solid #ccd; border-radius: 6px; box-sizing: border-box; }
  button { margin-top: 12px; padding: 10px 24px; font-size: 15px; cursor: pointer;
           background: #2f6db0; color: #fff; border: none; border-radius: 6px; }
  .result { margin: 14px 0; padding: 12px 16px; border-radius: 6px;
            border-left: 5px solid #ccc; background: #f6f8fb; }
  .covered { border-left-color: #2e9e5b; }
  .partial { border-left-color: #d9a441; }
  .gap     { border-left-color: #d1495b; }
  .status  { font-weight: 700; text-transform: uppercase; font-size: 12px;
             letter-spacing: 1px; }
  .cid { color: #667; font-size: 13px; }
  .ev { font-style: italic; color: #445; margin-top: 4px; font-size: 13px; }
  .summary { display: flex; gap: 20px; margin: 20px 0; font-weight: 600; }
</style></head>
<body>
  <h1>LACUNA</h1>
  <p class="sub">Control-gap analysis. Paste your security policies; see which ISO 27001 controls they address.</p>
  <form method="post">
    <textarea name="policy" placeholder="Paste policy text here...">{{ policy or '' }}</textarea>
    <button type="submit">Analyze gaps</button>
  </form>
  {% if results %}
    <div class="summary">
      <span style="color:#2e9e5b">Covered: {{ counts.covered }}</span>
      <span style="color:#d9a441">Partial: {{ counts.partial }}</span>
      <span style="color:#d1495b">Gaps: {{ counts.gap }}</span>
    </div>
    {% for r in results %}
      <div class="result {{ r.status }}">
        <span class="status">{{ r.status }}</span>
        <span class="cid">{{ r.control_id }} — {{ r.control_title }}</span>
        <div>{{ r.rationale }}</div>
        {% if r.evidence %}<div class="ev">Evidence: "{{ r.evidence }}"</div>{% endif %}
      </div>
    {% endfor %}
  {% endif %}
</body></html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    results = counts = policy = None
    if request.method == "POST":
        policy = request.form.get("policy", "").strip()
        if policy:
            results = analyze(policy)
            counts = {"covered": sum(r["status"] == "covered" for r in results),
                      "partial": sum(r["status"] == "partial" for r in results),
                      "gap": sum(r["status"] == "gap" for r in results)}
    return render_template_string(PAGE, results=results, counts=counts, policy=policy)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
