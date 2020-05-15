# import sys 
# import os
# path = os.path.join(os.getcwd(),'input.txt')
# input = open(path).readline

import numpy as np
S = input()
cand = np.zeros(2019,dtype=int)
rem = 0
order = 1
mod = 2019
for s in S[::-1]:
    rem += (int(s)*order)%mod
    rem %= mod
    cand[rem] +=1
    order *= 10
    order %=mod
ans = cand[0]
cand = cand[cand>1]
for c in cand:
    ans += c*(c-1)/2
print(int(ans))