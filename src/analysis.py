import re
import spacy

nlp = spacy.load("en_core_web_sm")

def classify_contract(text):
    text_lower = text.lower()
    if 'employment' in text_lower or 'salary' in text_lower:
        return "Employment Agreement"
    elif 'vendor' in text_lower or 'supply' in text_lower:
        return "Vendor Contract"
    elif 'lease' in text_lower or 'rent' in text_lower:
        return "Lease Agreement"
    elif 'partnership' in text_lower or 'share' in text_lower:
        return "Partnership Deed"
    else:
        return "Service Contract"  # Default

def extract_clauses(sentences):
    clauses = []
    for sent in sentences:
        if re.search(r'\b(clause|section|article)\b', sent.lower()):
            clauses.append(sent)
    return clauses if clauses else sentences[:10]  # Fallback to first 10 sentences

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['ORG', 'PERSON', 'MONEY', 'DATE', 'GPE']]
    return entities

def identify_obligations(text):
    obligations = []
    if 'shall' in text.lower():
        obligations.append("Obligations: Parties must perform as stated.")
    if 'right to' in text.lower():
        obligations.append("Rights: Parties have rights as specified.")
    if 'prohibited' in text.lower() or 'not allowed' in text.lower():
        obligations.append("Prohibitions: Certain actions are forbidden.")
    return "; ".join(obligations) if obligations else "No clear obligations identified."