import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    mod = 10**9+7
    h, w = mi()
    g = [[] for _ in range(h+1)]
    g[0] = '#'*(w+1)
    for i in range(h):
        g[i+1] = '#'+input()
    dp = np.zeros((h+1, w+1), dtype=int)
    dp[1][1] = 1
    for i in range(1, h+1):
        for j in range(1, w+1):
            if g[i][j] == '#':
                dp[i][j] = 0
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][j]+dp[i][j-1])
            dp[i][j] %= mod
    print(dp[h][w])
            
            

    


if __name__ == '__main__':
    main()