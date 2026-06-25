import subprocess
import platform

def run_cmd(cmd):
    if platform.system() != "Linux":
        return {"status": "ERROR", "error": "Run on Linux/WSL only"}

    try:
        output = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
        return {"status": "OK", "output": output.strip()}
    except subprocess.CalledProcessError as e:
        return {"status": "ERROR", "error": e.output.strip()}