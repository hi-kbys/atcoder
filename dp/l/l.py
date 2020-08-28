import sys
import numpy as np
from numba import njit
from numba.typed import List
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

n = ii()
a = li()
a = [List().append(x) for x in a]
cache = np.full((n, n), False, dtype=bool)
dp = np.zeros((n, n), dtype=int)

@njit(cache=True)
def dfs(i, j, cache, dp, a):
    if i == j: return a[i]
    if cache[i][j]:
        return dp[i][j]
    dp[i][j] = max(a[i]-dfs(i+1, j, cache, dp, a), a[j]-dfs(i, j-1, cache, dp, a))
    return dp[i][j]

dfs(0, n-1, cache, dp, a)
print(dp[0][n-1])
            
    