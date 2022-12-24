import os
import subprocess
from subprocess import PIPE
from shlex import quote
import time

def main():
    atcoder_username = os.environ["ATCODER_USERNAME"]
    atcoder_password = os.environ["ATCODER_PASSWORD"]

    url = "https://atcoder.jp"
    command = [
        "oj", "login",
        "-u", atcoder_username, "-p", atcoder_password, 
        "--check", url
        ]

    subprocess.run(command, capture_output = True, check=True)
    
if __name__ == "__main__":
    main()