# 📄 Contract Analysis & Risk Assessment Bot

Small and medium enterprises (SMEs) often sign legal contracts without fully understanding complex clauses, hidden risks, or unfavorable terms. Legal language is difficult to interpret, professional legal consultations are expensive, and risky clauses such as unilateral termination, indemnity, and non-compete are frequently overlooked, leading to financial loss and legal disputes.

The **Contract Analysis & Risk Assessment Bot** is a GenAI-powered legal assistant designed to help SMEs understand contracts in simple business language. The system analyzes uploaded contracts, extracts clauses, identifies potential legal risks, and provides clear explanations and recommendations before signing.

Key features include uploading contracts in TXT, DOCX, or PDF format, automatic clause extraction, clause-level risk classification (Low, Medium, High), plain-English explanation of risky clauses using GenAI, suggested safer alternatives for unfavorable clauses, an overall contract risk score, and a business-friendly contract summary. Sensitive data is handled securely and contracts are not stored.

The system is built using Python with NLP and rule-based analysis, Groq LLaMA models for GenAI reasoning, Streamlit for the user interface, and Streamlit Cloud for deployment.

System flow: a user uploads a contract file, text is extracted and segmented into clauses, each clause is analyzed for legal risk, the GenAI model explains risky clauses in simple language, and the system generates an overall risk score and summary.

Project structure:
ContractRiskBot/
- app.py  
- requirements.txt  
- utils/
  - file_loader.py  
  - clause_extractor.py  
  - risk_detector.py  
  - llm_helper.py  
- sample_contracts/
  - sample_medium_high_risk.txt  
- README.md  

To run locally, clone the repository, install dependencies using `pip install -r requirements.txt`, set the Groq API key using `setx GROQ_API_KEY "your_groq_api_key"` on Windows, and start the app with `streamlit run app.py`.

Live deployed application:
https://contractriskbot-revanthpb.streamlit.app

Demo video:
(Add your public YouTube or Google Drive demo link here)

This solution empowers Indian SMEs to identify legal risks before signing contracts, understand legal language without legal expertise, reduce dependency on costly legal consultations, and make informed and confident business decisions. API keys are managed securely using environment variables, and all contract processing happens in memory without persistent storage.
