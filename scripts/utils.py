from pathlib import Path
from urllib.request import urlopen
import json


def get_contest_id(args):
    # 実行ファイルがコンテストごとのフォルダか単体ファイルか判定する
    script_path = args[0]
    file_path = args[1]
    print(script_path, file_path)
    problem_id = contest_id = ''
    basedir_path = ''

    for i, char in enumerate(file_path):
        if script_path[i] == file_path[i]:
            continue
        else:
            basedir_path = file_path[:i]
            file_path = file_path[i:]
            break
    print('filepath:', file_path)
    # folder形式かfile単体か
    fs = file_path.split('/')
    if len(fs) == 3:
        parts = fs[-1].split('_')
        problem_id = parts.pop(-1).split('.')[0]
        contest_id = '_'.join(parts)
    if len(fs) == 4:
        contest_id = fs[-2]
        problem_id = fs[-1].split('.')[0]
    if len(fs) == 5:
        contest_id = fs[2]
        problem_id = fs[3]

    return basedir_path, contest_id, problem_id


def get_oj_url(contest_id, problem_id):
    oj_urls = []
    oj_urls.append("https://atcoder.jp/contests/{0}/tasks/{0}_{1}".format(contest_id, problem_id))
    oj_urls.append("https://atcoder.jp/contests/{0}/tasks/{1}_{2}".format(contest_id.replace('_', '-'),contest_id,problem_id))
    oj_urls.append("https://atcoder.jp/contests/{0}-open/tasks/{1}_{2}".format(contest_id.replace('_', '-'),contest_id,problem_id))

    url_flag = False
    for oj_url in oj_urls:
        try:
            urlopen(oj_url)
            url_flag = True
            break
        except Exception as e:
            print('Error :', e)
            print('URL not found:', oj_url)

    if not url_flag:
        oj_url = input('Please enter contest_url:')
    
    return oj_url


def get_acc_url(base_dir):
    contest_info_path = base_dir.parent/'contest.acc.json'
    if not contest_info_path.exists():
        return None
    with contest_info_path.open() as f:
        contest_info = json.loads(f.read())
    dir_name = base_dir.parts[-1]
    tasks = contest_info['tasks']
    for task in tasks:
        if not task.get('directory'):
            continue
        if task['directory']['path'] == dir_name:
            acc_url = task['url']
    return acc_url


if __name__ == '__main__':
    base_dir = Path('/workspaces/atcoder/field/other/typical90/003')
    print(get_acc_url(base_dir))
