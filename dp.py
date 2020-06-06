import copy
n = 3
A = [3,2,1]
A = [a - min(A) +1 for a in A]
dp = [0]*(max(A)+1)
lis = [[] for i in range(max(A)+1)]
for i in range(n):
    a = A[i]
    if dp[a-1]+1 > dp[a]:
        dp[a] = dp[a-1]+1
        lis[a] = copy.deepcopy(lis[a-1])
        lis[a].append(i)
lis = sorted(lis, key = lambda x:len(x))
print(len(lis[-1]))
print(' '.join(map(lambda x:str(x+1),lis[-1])))