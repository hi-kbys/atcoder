import math
from functools import lru_cache
import sys

def ncr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))


def merge(root,parent):
    if parent != -1:
        Ad = Ad.remove(parent)
    if Ad == []:
        ret = 1
    else:
        for child in Ad:
            coef = math.factorial(size(root)-1)
            ret = math.factorial(get_size(v)-1)
            ret *= dp(u,root)/math.factorial(size(u,root))
    return int(ret)   


input = sys.stdin.buffer.readline
N = int(input())

mod = 10**9 +7
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

order = []
stack = [1]
parent = [0]*(N+1)
while stack:
    node = stack.pop()
    order.append(node)
    for v in adj[node]:
        if v == parent[node]:
            continue
        stack.append(v)
        parent[v] = node
print(order)

size_d = [0]*(N+1)
dp_d = [1]*(N+1)

for v in order[::-1]:
    dp_d[v] *= fact[size_d[v]]
    dp_d[v] %= mod
    p = parent[v]
    s = size_d[v] + 1
    size_d[p] += s
    dp_d[p] *= fact_inv[s] * dp_d[v]
    dp_d[p] %= mod

for i in order[1:]:
        dp[i] = ncr(N,size[v])*dp[v]/(ncr(size[v]-1,size[i]))%mod
print(size[1:])
for i in dp[1:]:
    print(int(i))