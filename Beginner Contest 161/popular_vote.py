N,M = map(int,input().split())
A = list(map(int,input().split()))
shreshold = sum(A)/(4*M)
ret = [a for a in A if a >= shreshold]
if len(ret) < M:
    print('No')
else:
    print('Yes')