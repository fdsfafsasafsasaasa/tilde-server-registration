import subprocess
import crypt
import re

def check_username(username):
    if re.match(r"^[a-zA-Z]+$", username):
        return True
    else:
        return (False, "Username Check Failed")
    
def create_user(username, password, ssh_key, shell):
    try:
        subprocess.call(["sudo", "useradd", "-m", username, "-p", crypt.crypt(password)])
    except subprocess.CalledProcessError:
        return (False, "Unknown Error")
    
    try:
        subprocess.call(["sudo", "mkdir", f"/home/{username}/.ssh"])
    except subprocess.CalledProcessError:
        return (False, "Unknown Error")
    
    try:
        subprocess.call(["sudo", "echo", ssh_key, f"/home/{username}/.ssh/authorized_keys"])
    except subprocess.CalledProcessError:
        return (False, "Unknown Error")
    
    try:
        subprocess.call(["sudo", "chsh", "--shell", shell, username])
    except subprocess.CalledProcessError():
        return (False, "Unknown Error")
    return True