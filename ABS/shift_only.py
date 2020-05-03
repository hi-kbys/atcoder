import numpy as np

import sys 
import os
path = os.path.join(os.getcwd(),'input.txt')
input = open(path).readline

N = int(input())

#A = np.array(list(map(int,input().split())),dtype=int)
print(A)
ans = 0
while sum(A%2) == 0:
    A/=2
    ans +=1
print(ans)