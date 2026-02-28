def human_approval(recommendation: str) -> str:
    print("\n--- HUMAN APPROVAL REQUIRED ---")
    print(recommendation)
    decision = input("\nApprove this output? (yes/no): ").strip().lower()
    if decision == "yes":
        return recommendation
    return "Recommendation rejected by human reviewer."
