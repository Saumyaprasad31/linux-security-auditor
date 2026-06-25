from utils.runner import run_cmd

def run():
    result = run_cmd("cat /etc/ssh/sshd_config")

    return {
        "name": "SSH_CONFIG",
        "data": result.get("output", "")
    }