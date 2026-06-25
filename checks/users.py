from utils.runner import run_cmd

def run():
    result = run_cmd("cat /etc/passwd")

    return {
        "name": "USERS",
        "data": result.get("output", "")
    }