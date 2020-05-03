import sys

import os
path = os.getcwd()
path = os.path.join(path,"input.txt")
sys.stdin = open(path)

input = sys.stdin.readline
N = int(input())
H = list(map(int,input().split()))

dp = 0
i = 0
dp = [0]*(N)
for i in range(1,N):
    if i ==1:
        dp[i] = dp[i-1] + abs(H[i]-H[i-1])
        continue
    dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]),dp[i-2] + abs(H[i]-H[i-2]))

print(dp[N-1])
        