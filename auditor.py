import importlib
import os
import webbrowser
from datetime import datetime

from core.analyzer import analyze_check
from core.risk_engine import calculate_risk
from reports.generate_report import save_report


CHECKS = [
    "checks.firewall",
    "checks.open_ports",
    "checks.users",
    "checks.ssh_config"
]


def run_checks():
    all_findings = []
    total_score = 0

    for check in CHECKS:
        try:
            module = importlib.import_module(check)

            result = module.run()

            findings, score = analyze_check(
                result["name"],
                result["data"]
            )

            all_findings.extend(findings)
            total_score += score

        except Exception as e:
            all_findings.append({
                "name": check,
                "severity": "ERROR",
                "message": str(e)
            })

    return all_findings, total_score


def generate_html(report):
    html = f"""
    <html>
    <head>
        <title>Security Report</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            .HIGH {{ color: red; }}
            .MEDIUM {{ color: orange; }}
            .LOW {{ color: green; }}
            .box {{ border: 1px solid #ccc; padding: 10px; margin: 10px; }}
        </style>
    </head>
    <body>

    <h1>Linux Security Audit Report</h1>

    <h2>Risk: {report['risk']['level']}</h2>
    <h3>Score: {report['risk']['score']}</h3>

    <hr>
    <h2>Findings</h2>
    """

    for f in report["findings"]:
        html += f"""
        <div class="box">
            <h3>{f.get('id', f.get('name'))}</h3>
            <p class="{f.get('severity','LOW')}">
                {f.get('message','No details')}
            </p>
        </div>
        """

    html += "</body></html>"
    return html


def open_dashboard():
    path = os.path.abspath("reports/dashboard.html")
    webbrowser.open_new_tab(f"file:///{path}")


def main():
    print("[+] Running Security Audit...\n")

    findings, score = run_checks()

    risk = calculate_risk(score)

    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "risk": risk,
        "findings": findings
    }

    # SAVE JSON
    file_path = save_report(report)
    print("[+] Report saved:", file_path)

    # GENERATE HTML
    html = generate_html(report)

    os.makedirs("reports", exist_ok=True)

    with open("reports/dashboard.html", "w") as f:
        f.write(html)

    print("[+] Dashboard generated")

    # OPEN DASHBOARD
    open_dashboard()

    print("\n[+] DONE")


if __name__ == "__main__":
    main()
