import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

def main():
    n, m = mi()
    xd, yd = {0}, {0}
    lh = []
    lv = []
    for i in range(n):
        a, b, c = mi()
        lh.append((a, b, c))
        xd.add(a)
        xd.add(b)
        yd.add(c)
    for i in range(m):
        c, a, b = mi()
        lv.append((a, b, c))
        yd.add(a)
        yd.add(b)
        xd.add(c)
    xd = list(sorted(xd))
    yd = list(sorted(yd))
    mx, my = {}, {}
    for i, x in enumerate(xd):
        mx[x] = i
    for i, y in enumerate(yd):
        my[y] = i
    h = len(xd)
    w = len(yd)

    g = [[False]*(w+2) for _ in range(h+2)]
    wall = [[False]*w for _ in range(h)]
    for a, b, c in lh:
        a = mx[a]
        b = mx[b]
        c = my[c]
        for i in range(a, b+1):
            wall[i][c] = True
    for a, b, c in lv:
        a = my[a]*2
        b = my[b]*2
        c = mx[c]*2
        for i in range(a, b+1):
            wall[c][i] = True
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    xs, ys = mx[0], my[0]
    q = deque([(xs, ys)])
    ans = 0
    while q:
        x, y = q.popleft()
        if x == 0 or x == h+1 or y == 0 or y == w+1:
            print('INF')
            return
        ans += (xd[x]-xd[x-1])*(yd[y]-yd[y-1])

        for v in range(4):
            nx = x + dx[v]
            ny = y + dy[v]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if g[nx,ny]:
                continue
            g[nx,ny] = True
            q.append((nx, ny))
    print(ans)


if __name__ == '__main__':
    main()