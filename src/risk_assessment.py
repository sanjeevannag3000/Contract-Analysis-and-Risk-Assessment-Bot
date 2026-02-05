import re

RISK_KEYWORDS = {
    "penalty": "Penalty Clause",
    "indemnity": "Indemnity Clause",
    "termination": "Termination Clause",
    "arbitration": "Arbitration Clause",
    "auto-renewal": "Auto-Renewal Clause",
    "lock-in": "Lock-in Period",
    "non-compete": "Non-Compete Clause",
    "ip": "IP Transfer Clause"
}

def detect_risks(text, contract_type):
    risks = []
    text_lower = text.lower()
    for keyword, risk_type in RISK_KEYWORDS.items():
        if keyword in text_lower:
            risks.append(f"{risk_type} detected.")
    if 'ambiguous' in text_lower or 'unclear' in text_lower:
        risks.append("Ambiguity detected.")
    return "; ".join(risks) if risks else "No major risks detected."

def assess_risks(clauses):
    scores = []
    for clause in clauses:
        risk_count = sum(1 for keyword in RISK_KEYWORDS if keyword in clause.lower())
        if risk_count > 2:
            scores.append("High")
        elif risk_count > 0:
            scores.append("Medium")
        else:
            scores.append("Low")
    overall_score = "High" if scores.count("High") > len(scores)/2 else "Medium" if "Medium" in scores else "Low"
    return scores, overall_score