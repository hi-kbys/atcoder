import sys
import numpy as np

# import os
# path = os.getcwd()
# path = os.path.join(path,"input.txt")
# sys.stdin = open(path)

input = sys.stdin.readline
N,K = map(int,input().split())
h = [int(input()) for _ in range(N)]
h.sort()
ans = float("inf")
for i in range(N-K+1):
    ans = min(ans,h[i+K-1]-h[i])
print(ans)