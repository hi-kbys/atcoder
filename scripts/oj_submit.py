import os
from utils import get_oj_url, get_acc_url
import sys
import subprocess

from utils import *



def oj_submit(oj_url):
    cp = subprocess.run(['oj', 'submit', oj_url, sys.argv[1]])
    if cp.returncode != 0:
        print('oj submit failed. exit')
        sys.exit(1)

    return


def main():
    basedir_name, contest_id, problem_id = get_contest_id(sys.argv)
    oj_url = get_acc_url(Path(sys.argv[1]).parent)
    if oj_url is None:
        oj_url = get_oj_url(contest_id, problem_id)
    oj_submit(oj_url)


if __name__=='__main__':
    main()