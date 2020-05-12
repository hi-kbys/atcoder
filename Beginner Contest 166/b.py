N,K = map(int,input().split())
sunuke_dict = {}
for i in range(K):
    d = int(input())
    sunuke_dict[i] = list(map(int,input().split()))
ans = [1]*(N+1)
ans[0]  =0
for v in sunuke_dict.values():
    for v_ in v:
        if ans[v_] == 1:
            ans[v_] =0
print(sum(ans))