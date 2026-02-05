# Legal Assistant (Offline Version)

This offline tool analyzes English contracts for SMB owners using rule-based NLP.

## Setup
1. Install Python 3.8+.
2. Run `pip install -r requirements.txt`.
3. Download spaCy model: `python -m spacy download en_core_web_sm`.
4. Run: `streamlit run app.py`.

## Usage
- Upload an English contract (PDF/DOCX/TXT).
- View summary, risks, and templates.
- Export PDF.

## Limitations
- English only (no Hindi translation without APIs).
- Rule-based analysis may miss nuances.
- No generative AI; outputs are template-driven.