import platform

def get_os():
    system = platform.system().lower()

    if "windows" in system:
        return "windows"
    elif "linux" in system:
        return "linux"
    else:
        return "unknown"