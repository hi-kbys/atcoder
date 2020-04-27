from functools import lru_cache
N,K = map(int,input().split())
mod = 10**9 + 7
counts = [0]*(K)
ans = 0 
for x in range(K,0,-1):
    y = K//x
    counts[x-1] = y**N%mod
    if y >= 2:
        for i in range(2,y+1):
            counts[x-1] -=counts[i*x-1]%mod 
            counts[x-1] %= mod
    ans +=x*counts[x-1]% mod
    ans%=mod  
print(ans)