N,K = map(int,input().split())
c = N%K
print(min(c, abs(K-c)))