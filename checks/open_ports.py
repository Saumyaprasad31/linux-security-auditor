from utils.runner import run_cmd

def run():
    result = run_cmd("ss -tuln")

    return {
        "name": "OPEN_PORTS",
        "data": result.get("output", "")
    }