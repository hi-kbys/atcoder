from heapq import heappop, heappush 
def dijkstra(xs, ys, xg, yg,h,w,k,field):
    # que->(cost, x, y, direction)
    que = [(0, xs, ys, 0)]
    inf = 10 ** 6
    dp = [inf] * (h+1)*(w+1)*4
    visited = [[False for _ in range(w+1)] for _ in range(h+1)]
    dp[(xs*w+ys)*1] = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while que:
        cost, x, y, direction= heappop(que)
        # 現在のコストより高いなら無視する
        now = (x*w+y)*(direction+1)
        if cost > dp[now]:
            continue
        if x == xg and y == yg:
            print(cost)
            exit(0)
        for i in range(4):
            if i != direction:
                loc = (x*w+y)*(i+1)
                if dp[loc] > (dp[now]+k-1)//k:
                    dp[loc] = 

            x_, y_ = x+dx[i], y+dy[i]
            if not field[x_][y_]:
                break
            if dp[x_][y_] > dp[x][y] + 1:
                dp[x_][y_] = dp[x][y] + 1
                heappush(que, (dp[x_][y_], x_, y_))
        visited[x][y] = True
    print(-1)
        

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    h, w, k = map(int, input().split())
    xs, ys, xg, yg = map(int, input().split())
    field = [[False]*(w+2) for _ in range(h+2)]
    for i in range(h):
        # False で覆うことでx,yの制限をなくす。
        s = [True if _ == '.' else False for _ in input()]
        field[i+1] = [False]+s+[False]
    dijkstra(xs, ys, xg, yg, h, w, k, field)

if __name__ == '__main__':
    main()