def main():
    import sys
    input = sys.stdin.buffer.readline
    n,m = map(int, input().split())
    adj = [[] for i in range(n)]
    for i in range(m):
        a,b = map(lambda x: int(x)-1, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    que = [0]
    parent = [-1] * (n)
    while que:
        node = que.pop(0)
        for child in adj[node]:
            if parent[node] == child:
                continue
            if parent[child] == -1:
                que.append(child)
                parent[child] = node
    
    if -1 in parent[1:]:
        print('No')
    else:
        print('Yes')
    for p in parent[1:]:
        print(p+1)


if __name__ == '__main__':
    main()