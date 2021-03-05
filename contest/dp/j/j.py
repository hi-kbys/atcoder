import sys
from collections import Counter as cc
from numba import njit
import numpy as np

def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

# sys.setrecursionlimit(10**4)
n = ii()
a = li()
c = cc(a)
N = sum(c.values())
cache = np.full((N+1, N+1, N+1), -1, dtype=float)
cache[0][0][0] = 0
@njit(cache=True)
def dfs(x, y, z, N, cache):
    if x+y+z==0:
        return 0
    if cache[x][y][z]>=0:
        return cache[x][y][z]
    tmp = 1
    if x > 0:
        tmp += dfs(x-1, y, z,N, cache)*x/N
    if y > 0:
        tmp += dfs(x+1, y-1, z, N, cache)*y/N
    if z > 0:
        tmp += dfs(x, y+1, z-1, N, cache)*z/N
    tmp *= N/(x+y+z)
    cache[x][y][z] = tmp
    return tmp

dfs(c[1], c[2], c[3], N, cache)
print(cache[c[1]][c[2]][c[3]])
  