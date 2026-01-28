from utils.file_loader import load_file
import streamlit as st

from utils.clause_extractor import extract_clauses
from utils.risk_detector import detect_risk
from utils.llm_helper import explain_clause

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    text = load_file(uploaded_file)
    clauses = extract_clauses(text)

    high_risk_count = 0

    for clause in clauses:
        risk = detect_risk(clause["text"])
        if risk == "High":
            high_risk_count += 1

        with st.expander(f"{clause['clause_id']} - Risk: {risk}"):
            st.write(clause["text"])

            if risk != "Low":
                explanation = explain_clause(clause["text"], risk)
                st.markdown("### 🔍 Explanation")
                st.write(explanation)

    # ✅ Calculate overall risk score
    score = min(100, high_risk_count * 20)

    # ✅ SHOW SUMMARY HERE (ADD THIS PART)
    st.markdown("## 📌 Contract Summary (For Business Owners)")
    st.write(
        f"""
        • Total Clauses Analyzed: {len(clauses)}  
        • High Risk Clauses: {high_risk_count}  
        • Overall Risk Score: {score}/100  

        ⚠️ Recommendation: Review high-risk clauses carefully before signing.
        """
    )

    # ✅ Sidebar metric
    st.sidebar.metric("Overall Risk Score", f"{score}/100")