import re

def simple_retrieve_context(guidelines_text: str, query: str, max_chars: int = 1200) -> str:
    paragraphs = [p.strip() for p in guidelines_text.split("\n\n") if p.strip()]
    q_words = set(re.findall(r"[a-zA-Z]+", query.lower()))
    scored = []
    for p in paragraphs:
        words = set(re.findall(r"[a-zA-Z]+", p.lower()))
        overlap = len(q_words & words)
        if overlap > 0:
            scored.append((overlap, p))
    scored.sort(key=lambda x: x[0], reverse=True)

    selected = []
    total = 0
    for _, p in scored:
        if total + len(p) > max_chars:
            break
        selected.append(p)
        total += len(p)

    if not selected:
        return guidelines_text[:max_chars]
    return "\n\n".join(selected)
