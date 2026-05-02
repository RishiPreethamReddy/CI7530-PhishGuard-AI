# PhishGuard AI

## Project Title
**PhishGuard AI: An Agentic AI Assistant for Phishing Email Risk Assessment**

## Overview
PhishGuard AI is a cyber-security digital artefact created for the CI7530 Cyber and Artificial Intelligence Applications coursework. It helps users assess whether an email may be a phishing attempt by checking for common warning signs such as urgent language, suspicious links, account suspension threats, credential requests, payment pressure, and requests for sensitive information.

The tool gives:
- Risk score
- Risk level
- Detected warning signs
- Explanation
- Recommended action
- Human review warning

## Purpose
The purpose of this artefact is to support early-stage phishing email risk assessment. It is designed as a defensive support tool and does not replace human cyber-security judgement.

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
streamlit run app.py
```

### 3. Open the browser link shown in the terminal
Usually:
```text
http://localhost:8501
```

## Repository Structure
```text
CI7530-PhishGuard-AI/
│
├── README.md
├── app.py
├── requirements.txt
│
├── documentation/
│   ├── project_management.md
│   ├── testing_evidence.md
│   ├── handover_notes.md
│   ├── risk_analysis.md
│   └── gai_acknowledgement.md
│
├── sample_inputs/
│   ├── safe_email.txt
│   ├── suspicious_email.txt
│   └── high_risk_phishing_email.txt
│
└── screenshots/
    └── add_your_screenshots_here.txt
```

## Testing
The artefact should be tested using:
1. A normal safe email
2. A suspicious email with a link
3. A high-risk phishing email asking for password verification

## Limitations
This prototype mainly analyses email text. It does not currently check live URLs, attachments, email headers, sender authentication records, or real-time threat intelligence feeds.

## Future Improvements
- URL reputation checking
- Attachment scanning
- Email header analysis
- Machine learning classification
- Integration with Gmail/Outlook
- Security dashboard for analysts

## Ethical Notice
This artefact is designed for defensive cyber-security awareness and early-stage risk assessment only. It should not be used to create phishing emails or bypass security controls.
