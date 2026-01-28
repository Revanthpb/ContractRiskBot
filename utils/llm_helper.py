import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def explain_clause(clause_text, risk):
    prompt = f"""
You are a legal assistant for small business owners in India.

Explain the following contract clause in simple business English.

Risk Level: {risk}

Clause:
{clause_text}

Your response must include:
1. What this clause means
2. Why it may be risky
3. A safer or more balanced alternative
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return completion.choices[0].message.content