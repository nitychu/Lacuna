"""
Lacuna — retrieval engine.
Embeds policy text and control text into vectors, then for each control
finds the policy chunks most semantically similar to it.
"""
import os
import anthropic
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def chunk_text(text, max_chars=600):
    """Split a policy document into overlapping paragraph-ish chunks."""
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks, current = [], ""
    for p in paragraphs:
        if len(current) + len(p) < max_chars:
            current += " " + p
        else:
            if current:
                chunks.append(current.strip())
            current = p
    if current:
        chunks.append(current.strip())
    return chunks


def embed(texts):
    """
    Turn a list of strings into vectors using a simple bag-of-words
    hashing embedding. No external embedding model needed — deterministic,
    fast, and good enough for semantic-ish retrieval over policy text.
    """
    import hashlib
    DIM = 512
    vectors = []
    for t in texts:
        vec = np.zeros(DIM)
        words = t.lower().split()
        for w in words:
            h = int(hashlib.md5(w.encode()).hexdigest(), 16) % DIM
            vec[h] += 1
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        vectors.append(vec)
    return np.array(vectors)


def retrieve(control_text, policy_chunks, chunk_vectors, top_k=3):
    """Return the top_k policy chunks most similar to a control."""
    q = embed([control_text])
    sims = cosine_similarity(q, chunk_vectors)[0]
    ranked = sorted(enumerate(sims), key=lambda x: x[1], reverse=True)
    results = []
    for idx, score in ranked[:top_k]:
        results.append({"chunk": policy_chunks[idx], "score": float(score)})
    return results


if __name__ == "__main__":
    sample = "Our company requires multi-factor authentication for all administrator accounts.\nBackups are taken nightly and stored offsite.\nAll staff complete annual security training."
    chunks = chunk_text(sample)
    vecs = embed(chunks)
    hits = retrieve("Secure authentication technologies shall be implemented.", chunks, vecs)
    for h in hits:
        print(round(h["score"], 3), "->", h["chunk"][:70])
