import os 
import pathlib
dir_path = 'ABC/' + input()
os.mkdir(dir_path)
alph = [chr(ord('a')+i) for i in range(6)]
for el in alph:
    name = el + '.py'
    file = os.path.join(dir_path, el+'.py')
    pathlib.Path(file).touch()
