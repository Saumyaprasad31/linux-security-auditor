from checks.os_detect import get_os

def check_world_writable():

    if get_os() != "linux":
        return {
            "status": "skipped",
            "reason": "find command only on Linux"
        }

    return {
        "status": "real",
        "note": "Would scan world writable files"
    }