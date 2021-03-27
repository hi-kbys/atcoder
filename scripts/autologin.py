import os
import subprocess
from subprocess import PIPE
from shlex import quote
import time

atcoder_username = os.environ["ATCODER_USERNAME"]
atcoder_password = os.environ["ATCODER_PASSWORD"]

command = "oj login https://atcoder.jp"
with subprocess.Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE,text=True) \
    as proc:
    while proc.poll() is None:
        o = proc.stdout.readline()
        print(o)
        if o == '[NETWORK] 200 OK\n':
            break
    inputs = atcoder_username+'\n'+atcoder_password+'\n'
    try:
        stdout, stderr = proc.communicate(inputs,1)
    except :
        print(stdout)
        print(stderr)
    proc.communicate(inputs,1)
    
print('owari')
