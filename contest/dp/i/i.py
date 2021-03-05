import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

def main():
    n = ii()
    p = list(map(float, input().split()))
    dp = np.zeros((n+1, n+1), dtype=float)
    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0]*(1-p[i-1])
        for j in range(1, n+1):
            dp[i][j] = p[i-1]*dp[i-1][j-1] + (1-p[i-1])*dp[i-1][j]
    print(np.sum(dp[-1][n//2+1:]))
    

if __name__ == '__main__':
    main()