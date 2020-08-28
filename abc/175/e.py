import sys
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

import numpy as np
def main():
    r, c, k = mi()
    g = np.zeros((r+1, c+1), dtype=int)
    for _ in range(k):
        i, j, v = mi()
        g[i][j] = v
    dp = np.zeros((r+1,c+1,4), dtype=int)
    for i in range(1, r+1):
        for j in range(1, c+1):
            for k in range(4):
                dp[i][j][k] = max(dp[i][j-1][k], dp[i-1][j][3])
            if g[i][j] > 0:
                for k in range(2, -1, -1):
                    dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k]+g[i][j])

    print(dp[r][c][3])


if __name__ == '__main__':
    main()