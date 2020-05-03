import sys
import numpy as np

import os
path = os.getcwd()
path = os.path.join(path,"input.txt")
sys.stdin = open(path)

input = sys.stdin.readline
N,W  = map(int,input().split())
dp = np.zeros((N+1,W+1),dtype=int)
w,v = [],[]
for _ in range(N):
    w_,v_ = map(int,input().split())
    w.append(w_)
    v.append(v_)

for row in range(N):
    dp[row+1,:w[row]] = dp[row,:w[row]]
    dp[row+1,w[row]:] = np.maximum(dp[row,w[row]:],v[row]+dp[row,:-w[row]])
print(dp[N,-1])