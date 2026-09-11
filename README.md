# Lacuna

A control-gap analyzer. Point it at an organization's written security policies and it reports which ISO 27001:2022 controls they address, which they only partially address, and which they miss entirely — with a rationale and cited evidence for each verdict.

![Lacuna results](screenshot.png)

## The problem it solves

Gap analysis is a standard GRC task: an organization has a pile of policies, a framework says "you must address X, Y, Z," and someone has to read everything and find what is missing. By hand it is slow and inconsistent. With keyword search it is wrong — a policy that says "staff verify their identity with a second factor" clearly addresses the authentication control, but the word "authentication" never appears, so keyword matching calls it a gap.

That mismatch is why this uses retrieval over embeddings rather than string matching: semantic similarity catches that a policy covers a control even when the wording differs.

## How it works

1. A set of real ISO 27001:2022 Annex A controls serves as the expected checklist.
2. Uploaded policy text is split into chunks and embedded into vectors.
3. For each control, the most semantically similar policy chunks are retrieved by cosine similarity.
4. An LLM reads the control and the retrieved excerpts and returns a verdict: covered, partial, or gap, with a one-line rationale and the most relevant phrase as evidence.
5. A web page shows the verdicts color-coded, with a summary count.

The three-way verdict is the design choice that matters most. Binary covered/not-covered would be dishonest — most real policies touch a control without fully satisfying it. "Partial" is where the actual audit findings live.

## Stack

Python, Flask, the Anthropic API for the judgment layer, scikit-learn for cosine similarity.

## Honest limitations

- The embedding is lexical-semantic, not neural. It uses a deterministic bag-of-words hashing vector, not a trained embedding model. This was a deliberate trade to keep the tool dependency-light and reproducible: retrieval catches word-overlap and near-paraphrase well but misses deep conceptual matches a neural embedding would get. Swapping in a real embeddings API is a one-function change and is the obvious next step.
- The control set is a representative subset, not all 93 Annex A controls. The pipeline handles the full set unchanged; the subset keeps analysis fast and the demo readable.
- The verdict is a judgment, not an authority. The tool accelerates a human reviewer, it does not replace one. "Covered" means the policy plausibly addresses the control's intent, not that the organization is compliant.
- No evidence of implementation. Like any policy-based analysis, this checks what the documents say, not what the organization does. Written coverage is necessary but not sufficient for actual control effectiveness.

## What I would add next

Real neural embeddings; the full Annex A control set; support for multiple documents and multiple frameworks; and an export to an audit-ready findings format.
