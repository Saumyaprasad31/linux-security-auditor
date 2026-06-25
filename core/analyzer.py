from core.rules import RULES

def analyze_check(name, output):
    findings = []
    score = 0

    for rule in RULES:
        try:
            if rule["check"](output):
                findings.append({
                    "id": rule["id"],
                    "name": name,
                    "severity": rule["severity"],
                    "message": rule["message"]
                })

                score += rule["score"]

        except:
            continue

    return findings, score