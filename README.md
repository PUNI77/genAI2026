# Personal Healthcare & Nutrition Coach (Academic Version)

This is a simple, **college-project-friendly** implementation of a Personal Healthcare & Nutrition Coach.

## Features (3 Required Criteria)

1. **No hallucinations (RAG grounded)**
   - The assistant only answers from retrieved guideline text.
   - If information is missing, it says so.

2. **Automatic tool selection**
   - Agent decides between:
     - Calorie Calculator
     - Nutrition Search tool

3. **Human-in-the-Loop (HITL)**
   - A human must approve the final output before it is shown.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your guideline PDF:
```
data/nutrition_guidelines.pdf
```

3. Run:
```bash
python app.py
```
