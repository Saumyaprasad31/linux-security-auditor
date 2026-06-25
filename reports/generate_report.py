import json
from datetime import datetime

def save_report(data):
    filename = f"reports/audit_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    return filename