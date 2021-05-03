import subprocess
import crypt
import re

def check_username(username):
    if not re.match(r"[^a-zA-Z0-9]", username):
        return True
    else:
        return False
    
def create_user(username, password, ssh_key):
    try:
        subprocess.call(["sudo", "useradd", "-m", username, "-p", crypt.crypt(password)])
    except subprocess.CalledProcessError:
        return False
    
    try:
        subprocess.call(["mkdir", f"/home/{username}/.ssh"])
    except subprocess.CalledProcessError:
        return False
    
    subprocess.call(["sudo", "echo", ssh_key, "/home/{username}/.ssh/authorized_keys"])

    return True