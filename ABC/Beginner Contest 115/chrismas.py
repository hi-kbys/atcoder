import sys
import numpy as np

import os
path = os.getcwd()
path = os.path.join(path,"input.txt")
sys.stdin = open(path)

input = sys.stdin.readline
N,X = map(int,input().split())
loc = 2**(N+2)- 3
loc = (loc-1)/2 + 1
ans = 0
while N>=0:
    if X >= loc:
        X -= loc
        if loc ==1:
            print("hey")
            ans += 1
        else:
            ans += 2**(N-1) 
    else:
        X -= 1
    N -= 1
    loc = (loc-3)/2 + 1
print(ans)      