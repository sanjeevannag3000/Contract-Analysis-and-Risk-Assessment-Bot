import streamlit as st
import os
from src.text_extraction import extract_text
from src.preprocessing import preprocess_text
from src.translation import check_language  # Simplified to check only
from src.analysis import classify_contract, extract_clauses, extract_entities, identify_obligations
from src.risk_assessment import detect_risks, assess_risks
from src.output_generation import generate_summary, generate_template, export_pdf
from utils.helpers import load_json, save_json

st.title("Legal Assistant for SMB Owners (Offline Version)")
st.sidebar.header("Upload Contract (English Only)")

uploaded_file = st.sidebar.file_uploader("Upload PDF, DOCX, or TXT", type=["pdf", "docx", "txt"])
if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1]
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Extract and process text
    raw_text = extract_text("temp_file", file_type)
    if not check_language(raw_text):
        st.error("Please provide an English contract. Hindi support removed to avoid APIs.")
        st.stop()
    
    sentences, cleaned_text = preprocess_text(raw_text)
    
    # Analysis
    contract_type = classify_contract(raw_text)
    clauses = extract_clauses(sentences)
    entities = extract_entities(raw_text)
    obligations = identify_obligations(raw_text)
    risks = detect_risks(raw_text, contract_type)
    risk_scores, overall_score = assess_risks(clauses)
    
    # Outputs
    summary = generate_summary({"type": contract_type, "entities": entities, "risks": risks})
    template = generate_template(contract_type)
    
    # Display
    st.header("Contract Summary")
    st.write(summary)
    st.header("Risk Assessment")
    st.write(f"Overall Risk: {overall_score}")
    for i, (clause, score) in enumerate(zip(clauses, risk_scores)):
        st.write(f"Clause {i+1}: {clause[:100]}... Risk: {score}")
    st.header("Suggested Template")
    st.write(template)
    
    # Export
    if st.button("Export PDF"):
        export_pdf(summary, "contract_analysis.pdf")
        st.download_button("Download PDF", data=open("contract_analysis.pdf", "rb"), file_name="contract_analysis.pdf")
    
    # Update knowledge base and audit log
    kb = load_json("data/knowledge_base.json")
    kb.append({"issue": risks[:50], "frequency": 1})  # Anonymized
    save_json("data/knowledge_base.json", kb)
    
    audit = load_json("data/audit_log.json")
    audit.append({"timestamp": "2023-10-01", "action": "analyzed_contract", "risk_score": overall_score})
    save_json("data/audit_log.json", audit)
    
    os.remove("temp_file")