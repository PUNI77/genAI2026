def judge_output(recommendation: str, context: str) -> str:
    banned_claims = ["cure", "guaranteed", "replace medication"]
    lower = recommendation.lower()
    for b in banned_claims:
        if b in lower:
            return f"UNSAFE: contains prohibited claim '{b}'"
    if len(context.strip()) == 0:
        return "UNSAFE: no guideline context"
    return "SAFE"
