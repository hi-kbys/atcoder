import sys

# import os
# path = os.getcwd()
# path = os.path.join(path,"input.txt")
# sys.stdin = open(path)

input = sys.stdin.readline
N,K = map(int,input().split())
H = list(map(int,input().split()))
dp = [float('inf')]*(K)
dp.append(0)
dp = dp[::-1]
for i in range(N-1):
    dp_ = dp.pop(0)
    if i >= N-K-1:
        dp = [min(dp_+abs(H[i+j+1]-H[i]),dp[j]) for j in range(N-i-1)]
        continue
    dp = [min(dp_+abs(H[i+j+1]-H[i]),dp[j])  for j in range(K)]
    dp.append(float("inf"))

print(dp[0])