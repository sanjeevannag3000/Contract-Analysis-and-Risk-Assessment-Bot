from reportlab.pdfgen import canvas

def generate_summary(analysis):
    template = f"Contract Type: {analysis['type']}. Key Entities: {analysis['entities']}. Risks: {analysis['risks']}. This is a simplified summary for SMB owners."
    return template

def generate_template(contract_type):
    templates = {
        "Employment": "This agreement outlines the terms of employment, including duties, salary, and termination conditions. Key points: Mutual consent for changes, fair notice periods.",
        "Vendor": "This vendor contract specifies deliverables, payment terms, and liabilities. Key points: Clear performance metrics, balanced indemnities.",
        "Lease": "This lease agreement covers rental terms, duration, and maintenance. Key points: Reasonable rent, mutual termination options.",
        "Partnership": "This partnership deed defines roles, profit sharing, and dissolution. Key points: Equal rights, clear exit clauses.",
        "Service": "This service contract details scope, timelines, and payments. Key points: Defined deliverables, fair penalties."
    }
    return templates.get(contract_type, "Standard template not available.")

def export_pdf(content, filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, content[:1000])  # Truncate for demo
    c.save()