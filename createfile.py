import os 
import pathlib
num = int(input())
dir_path = 'ABC/Beginner Contest {}'.format(num)
os.mkdir(dir_path)
alph = [chr(ord('a')+i) for i in range(6)]
for el in alph:
    name = el + '.py'
    file = os.path.join(dir_path,el+'.py')
    pathlib.Path(file).touch()
