import numpy as np
N, M = map(int,input().split())
H = np.array(list(map(int,input().split())))

adj = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(lambda x: int(x) -1 ,input().split())
    if a in adj[b]:
        continue
    adj[a].append(b)
    adj[b].append(a)

ans = 0 
for i, item in enumerate(adj):
     if item == []:
         ans+=1
         continue
     adj_max = max(H[item])
     if H[i] > adj_max:
         ans += 1
print(ans)