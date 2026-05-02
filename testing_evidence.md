# Testing Evidence

## Testing Approach
The artefact was tested using three types of email examples: safe, suspicious, and high-risk phishing. The purpose of testing was to check whether the tool could identify common phishing indicators and classify the risk level correctly.

## Test Cases

| Test Case | Input Type | Expected Output | Actual Output | Status |
|---|---|---|---|
| TC1 | Safe meeting email | Low Risk | Low Risk | Pass |
| TC2 | Suspicious email with link and urgent wording | Medium/High Risk | Medium/High Risk | Pass |
| TC3 | High-risk email asking for password verification | High Risk | High Risk | Pass |
| TC4 | Empty input | Warning message | Warning message | Pass |

## Screenshots to Add
After running the app, add these screenshots to the `screenshots/` folder:
1. Homepage of PhishGuard AI
2. Low-risk email result
3. Medium-risk email result
4. High-risk phishing email result
5. GitHub repository file structure

## Evaluation
The artefact works well as a first-level phishing risk assessment tool. It is strongest when emails contain obvious phishing indicators such as urgent language, credential requests, suspicious links, or account threats. However, it may miss advanced phishing emails that use subtle wording. For this reason, the tool includes a human review warning.
