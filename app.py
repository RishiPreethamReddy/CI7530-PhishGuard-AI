import re
from datetime import datetime
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="PhishGuard AI",
    page_icon="🛡️",
    layout="wide"
)


INDICATORS = {
    "Urgency / pressure": {
        "weight": 15,
        "patterns": [
            r"\bimmediately\b", r"\bact now\b", r"\burgent\b", r"\blast chance\b",
            r"\bfinal warning\b", r"\bwithin 24 hours\b", r"\btoday\b", r"\basap\b"
        ],
        "explanation": "The email uses urgent or pressuring language to make the user act quickly."
    },
    "Account threat": {
        "weight": 20,
        "patterns": [
            r"\baccount.*suspend", r"\baccount.*locked", r"\bpermanent closure\b",
            r"\bdeactivate", r"\bunauthori[sz]ed login\b", r"\bsecurity alert\b"
        ],
        "explanation": "The email threatens account suspension, closure, or unauthorised access."
    },
    "Credential request": {
        "weight": 25,
        "patterns": [
            r"\bpassword\b", r"\blogin details\b", r"\bverify.*account\b",
            r"\bconfirm.*identity\b", r"\benter.*credentials\b", r"\bOTP\b",
            r"\bone[- ]time pass(code|word)\b"
        ],
        "explanation": "The email asks for credentials or identity verification, which is a common phishing sign."
    },
    "Financial pressure": {
        "weight": 20,
        "patterns": [
            r"\bpayment\b", r"\binvoice\b", r"\bbank\b", r"\brefund\b",
            r"\btransaction\b", r"\bfine\b", r"\btax\b", r"\bbilling\b"
        ],
        "explanation": "The email mentions money, payments, banking, refunds, or financial pressure."
    },
    "Suspicious link": {
        "weight": 20,
        "patterns": [
            r"http[s]?://", r"\bbit\.ly\b", r"\btinyurl\b", r"\blogin[-_.]?\w*\.",
            r"\bverify[-_.]?\w*\.", r"\bsecure[-_.]?\w*\."
        ],
        "explanation": "The email contains a link or link wording that may lead to a fake website."
    },
    "Sensitive information request": {
        "weight": 20,
        "patterns": [
            r"\bcard number\b", r"\bCVV\b", r"\bdate of birth\b", r"\bnational insurance\b",
            r"\bpassport\b", r"\baddress\b", r"\bpersonal information\b"
        ],
        "explanation": "The email asks for personal or sensitive information."
    },
    "Attachment warning": {
        "weight": 15,
        "patterns": [
            r"\battachment\b", r"\bdownload\b", r"\bopen the file\b",
            r"\bmacro\b", r"\bzip file\b", r"\b.exe\b"
        ],
        "explanation": "The email encourages opening or downloading an attachment."
    },
    "Generic greeting": {
        "weight": 8,
        "patterns": [
            r"\bdear user\b", r"\bdear customer\b", r"\bhello customer\b",
            r"\bvalued customer\b"
        ],
        "explanation": "The email uses a generic greeting instead of addressing the recipient personally."
    }
}


def analyse_email(email_text: str):
    """Analyse email text and return risk score, risk level, indicators and recommendation."""
    text = email_text.lower()
    found = []
    score = 0

    for name, info in INDICATORS.items():
        matched_patterns = []
        for pattern in info["patterns"]:
            if re.search(pattern, text, flags=re.IGNORECASE):
                matched_patterns.append(pattern)
        if matched_patterns:
            score += info["weight"]
            found.append({
                "Indicator": name,
                "Risk Points": info["weight"],
                "Reason": info["explanation"]
            })

    url_count = len(re.findall(r"http[s]?://", email_text, flags=re.IGNORECASE))
    if url_count >= 2:
        score += 10
        found.append({
            "Indicator": "Multiple links",
            "Risk Points": 10,
            "Reason": "The email contains multiple links, which can increase phishing risk."
        })

    exclamation_count = email_text.count("!")
    if exclamation_count >= 3:
        score += 5
        found.append({
            "Indicator": "Excessive punctuation",
            "Risk Points": 5,
            "Reason": "The email uses repeated punctuation, often used to create panic or urgency."
        })

    score = min(score, 100)

    if score >= 70:
        level = "High Risk"
        recommendation = (
            "Do not click any links, do not download attachments, and do not enter login or payment details. "
            "Report the email to the IT/security team and verify the sender using an official channel."
        )
    elif score >= 35:
        level = "Medium Risk"
        recommendation = (
            "Treat this email with caution. Verify the sender, avoid clicking links until confirmed, "
            "and ask IT/security if you are unsure."
        )
    else:
        level = "Low Risk"
        recommendation = (
            "No major phishing indicators were detected, but still check the sender address and context before responding."
        )

    return score, level, found, recommendation


def build_report(score, level, found, recommendation):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    indicators = "\n".join([f"- {item['Indicator']}: {item['Reason']}" for item in found]) or "- No major indicators detected."
    return f"""PhishGuard AI Assessment Report
Generated: {now}

Risk Score: {score}/100
Risk Level: {level}

Detected Warning Signs:
{indicators}

Recommended Action:
{recommendation}

Human Review Warning:
This tool is a defensive support artefact. It does not replace professional cyber-security judgement.
"""


st.title("🛡️ PhishGuard AI")
st.subheader("Agentic AI Assistant for Phishing Email Risk Assessment")

st.info(
    "Paste an email below and click Analyse Email. The tool will check for common phishing warning signs "
    "and produce a risk score, explanation, and recommended action."
)

with st.expander("About this artefact"):
    st.write(
        "PhishGuard AI is a coursework artefact for CI7530 Cyber and Artificial Intelligence Applications. "
        "It is designed as a defensive support tool for early-stage phishing risk assessment. "
        "It uses transparent rules and AI-style reasoning steps so the result can be explained during handover."
    )

sample = """Dear user,

Your account will be suspended today unless you verify your password immediately.
Click the link below to confirm your login details:

http://secure-account-verification-login.com

Failure to act now will result in permanent account closure.
"""

email_text = st.text_area(
    "Paste email content here:",
    value="",
    height=260,
    placeholder=sample
)

col1, col2 = st.columns([1, 1])
with col1:
    analyse_button = st.button("Analyse Email", type="primary", use_container_width=True)
with col2:
    clear_button = st.button("Clear", use_container_width=True)

if clear_button:
    st.rerun()

if analyse_button:
    if not email_text.strip():
        st.warning("Please paste an email message before analysing.")
    else:
        score, level, found, recommendation = analyse_email(email_text)

        st.markdown("---")
        st.header("Assessment Result")

        metric_col1, metric_col2 = st.columns(2)
        metric_col1.metric("Risk Score", f"{score}/100")
        metric_col2.metric("Risk Level", level)

        if level == "High Risk":
            st.error("This email contains several strong phishing indicators.")
        elif level == "Medium Risk":
            st.warning("This email contains some suspicious indicators.")
        else:
            st.success("No major phishing indicators were detected.")

        st.subheader("Detected Warning Signs")
        if found:
            df = pd.DataFrame(found)
            st.dataframe(df, use_container_width=True)
        else:
            st.write("No major warning signs were detected by the current rule set.")

        st.subheader("Recommended Action")
        st.write(recommendation)

        st.subheader("Agentic Reasoning Steps")
        st.write("1. Read the email content.")
        st.write("2. Identify suspicious language, links, credential requests, and pressure tactics.")
        st.write("3. Assign risk points for each detected indicator.")
        st.write("4. Classify the email into Low, Medium, or High risk.")
        st.write("5. Provide a safe recommended action for the user.")

        st.subheader("Human Review Warning")
        st.write(
            "This artefact is a support tool only. It may produce false positives or false negatives. "
            "Important decisions should be reviewed by a human security professional."
        )

        report = build_report(score, level, found, recommendation)
        st.download_button(
            label="Download Assessment Report",
            data=report,
            file_name="phishguard_ai_assessment_report.txt",
            mime="text/plain"
        )
