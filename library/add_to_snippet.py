import os 
import pathlib
import sys



def main():
    cwd = os.getcwd()
    print(os.getcwd())
    path = os.path.join(cwd+'/python')
    files = os.listdir(path)
    print(files)
    for file in files:
        with open(os.path.join(path, file)) as f:
            contents.append(f.readlines())
    
    snippetfile = os.path('/home/kobyashi/atcoder/.vscode/\
            template-lib.code-snippets')
    with open(snippetfile) as f:
        for content in contents:
            for line 


if __name__ == "__main__":
    main()