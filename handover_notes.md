# Handover Notes

## Artefact Name
PhishGuard AI

## Purpose
PhishGuard AI helps users assess whether an email may be a phishing attempt. It gives a risk score, risk level, warning signs, explanation, and recommended action.

## How to Install
```bash
pip install -r requirements.txt
```

## How to Run
```bash
streamlit run app.py
```

## Main Files
- `app.py`: Main application code
- `requirements.txt`: Required Python packages
- `README.md`: Project overview and running instructions
- `sample_inputs/`: Test email examples
- `documentation/`: Supporting coursework documentation
- `screenshots/`: Evidence of the artefact working

## Important Limitations
The artefact is a prototype. It does not check email headers, attachments, live URL reputation, or threat intelligence databases. It should be used as a support tool, not as a final decision-maker.

## Future Improvements
- Add URL reputation checks
- Add attachment scanning
- Add sender domain checks
- Add machine learning classifier
- Add organisation dashboard
