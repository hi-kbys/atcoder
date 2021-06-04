import os
from utils import get_oj_url, get_contest_id, get_acc_url
import sys
import subprocess
from urllib.request import urlopen
from pathlib import Path
# from utils import get_contest_id,


def oj_download(tmp_path, oj_url):
    cp = subprocess.run(['oj', 'd', oj_url, '--format', '{}/sample-%i.%e'.format(tmp_path)])
    if cp.returncode != 0:
        print('oj download failed. exit')
        sys.exit(1)

    return


def oj_test(tmp_path):
    if sys.argv[1].split('.')[-1]=='cpp':
        cp = subprocess.run(['g++',sys.argv[1],'-o','./a.out'])
        cp = subprocess.run(['oj','t','-c','./a.out','-d',tmp_path,'-i','--print-memory'])
        os.remove('./a.out')
    else:    
        cp = subprocess.run(['oj','t','-c','python {}'.format(sys.argv[1]),'-d',tmp_path,'-i','--print-memory'])
    if cp.returncode != 0:
        print('oj test failed. exit')
        sys.exit(1)

    return

def main():
    basedir_path, contest_id, problem_id = get_contest_id(sys.argv)
    oj_url = get_acc_url(Path(sys.argv[1]).parent)
    
    if oj_url is None:
        oj_url = get_oj_url(contest_id, problem_id)
    tmp_path = '{}tmp/{}_{}'.format(basedir_path, contest_id, problem_id)
    
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)
    if not os.listdir('{}/.'.format(tmp_path)):
        oj_download(tmp_path, oj_url)

    oj_test(tmp_path)


if __name__=='__main__':
    main()