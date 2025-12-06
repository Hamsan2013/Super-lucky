import subprocess
import shlex

def run_command(cmd):
    try:
        p = subprocess.run(
            shlex.split(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return p.stdout if p.stdout else p.stderr
    except Exception as e:
        return str(e)

def is_dangerous(cmd):
    bad = ["rm ", "sudo", "shutdown", "reboot", "mkfs", "dd "]
    for b in bad:
        if b in cmd.lower():
            return True
    return False
