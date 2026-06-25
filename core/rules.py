RULES = [
    {
        "id": "FIREWALL_DISABLED",
        "check": lambda data: "inactive" in data.lower(),
        "severity": "HIGH",
        "score": 40,
        "message": "Firewall is disabled"
    },
    {
        "id": "ROOT_LOGIN_SSH",
        "check": lambda data: "permitrootlogin yes" in data.lower(),
        "severity": "HIGH",
        "score": 50,
        "message": "Root login enabled in SSH"
    },
    {
        "id": "PASSWORD_AUTH_ENABLED",
        "check": lambda data: "passwordauthentication yes" in data.lower(),
        "severity": "MEDIUM",
        "score": 25,
        "message": "Password authentication enabled"
    }
]