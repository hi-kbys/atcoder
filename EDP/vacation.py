import sys
import numpy as np

import os
path = os.getcwd()
path = os.path.join(path,"input.txt")
sys.stdin = open(path)

input = sys.stdin.readline
N = int(input())
abc = np.zeros((N,3))
for i in range(N):
    abc[i] = list(map(int,input().split()))

dp = np.zeros((N,3))
for i in range(N):
    if i == 0:
        dp[i] = abc[i]
        continue
    dp_a,dp_b,dp_c = dp[i-1]
    dp[i] = abc[i] + [max(dp_b,dp_c),max(dp_a,dp_c),max(dp_a,dp_b)]
print(int(max(dp[N-1])))
