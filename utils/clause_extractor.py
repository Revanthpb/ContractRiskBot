import re

def extract_clauses(text):
    clauses = []
    parts = re.split(r'\n\d+[\.\)]\s', text)

    for i, part in enumerate(parts):
        if len(part.strip()) > 40:
            clauses.append({
                "clause_id": f"C{i+1}",
                "text": part.strip()
            })

    return clauses