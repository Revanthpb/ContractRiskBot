def load_file(file):
    # PDF handling (safe import)
    if file.name.endswith(".pdf"):
        try:
            import pdfplumber
        except ImportError:
            return "PDF parsing not available. Please upload a TXT or DOCX file."

        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    # DOCX handling
    elif file.name.endswith(".docx"):
        try:
            import docx
        except ImportError:
            return "DOCX support not available."
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    # TXT handling
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        return ""