"""
Lacuna — retrieval engine.
Splits a policy into sections, embeds sections and control text as
lexical vectors, and finds the sections most relevant to each control.
Lexical (hashed bag-of-words), not neural.
"""
import os
import re
import hashlib
import anthropic
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

DIM = 4096

STOP = set("""
a an the and or of to in for on by with as at be is are was were will must
shall should may can this that these those it its their them they all any
each such from into than then also not no other our we us which who whom
has have had been being do does per via both within across based upon
including include includes ensure ensures ensuring information security
organization organizational policy policies procedure procedures
appropriate relevant requirement requirements
""".split())

SUFFIXES = ("ations", "ation", "ators", "ator", "ings", "ing", "ions", "ion",
            "ed", "es", "ly", "s")


def stem(w):
    for suf in SUFFIXES:
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


def tokenize(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [stem(w) for w in words if w not in STOP and len(w) > 2]


def is_heading(line):
    if len(line) > 50 or len(line.split()) > 8:
        return False
    if line[-1] in ".,:;" or not line[0].isupper():
        return False
    if any(ch.isdigit() for ch in line):
        return False
    return True


def chunk_text(text, max_chars=1500):
    """Split a policy into chunks by section heading, heading kept in each chunk."""
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    lines = [l for l in lines if not re.match(r"^Page \d+ of \d+$", l)]

    sections, heading, body = [], "", []
    for line in lines:
        if is_heading(line):
            if body:
                sections.append((heading, " ".join(body)))
            heading, body = line, []
        else:
            body.append(line)
    if body:
        sections.append((heading, " ".join(body)))

    chunks = []
    for heading, body in sections:
        prefix = heading + ": " if heading else ""
        while len(body) > max_chars:
            cut = body.rfind(". ", 0, max_chars)
            cut = cut + 1 if cut > 0 else max_chars
            chunks.append(prefix + body[:cut].strip())
            body = body[cut:].strip()
        if body:
            chunks.append(prefix + body)
    return chunks


def embed(texts):
    """Hashed bag-of-words vectors over cleaned, stemmed tokens."""
    vectors = []
    for t in texts:
        vec = np.zeros(DIM)
        for w in tokenize(t):
            h = int(hashlib.md5(w.encode()).hexdigest(), 16) % DIM
            vec[h] += 1
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        vectors.append(vec)
    return np.array(vectors)


def retrieve(control_text, policy_chunks, chunk_vectors, top_k=5):
    """Return the top_k policy chunks most similar to a control."""
    q = embed([control_text])
    sims = cosine_similarity(q, chunk_vectors)[0]
    ranked = sorted(enumerate(sims), key=lambda x: x[1], reverse=True)
    return [{"chunk": policy_chunks[i], "score": float(s)} for i, s in ranked[:top_k]]


if __name__ == "__main__":
    sample = ("Awareness and Training\nAll staff complete annual security training.\n"
              "Contingency Planning\nBackups are taken nightly and stored offsite.\n"
              "Identification and Authentication\nAdministrators use multi-factor authentication.")
    chunks = chunk_text(sample)
    vecs = embed(chunks)
    for h in retrieve("Personnel shall receive security awareness training.", chunks, vecs, top_k=3):
        print(round(h["score"], 3), "->", h["chunk"][:70])
