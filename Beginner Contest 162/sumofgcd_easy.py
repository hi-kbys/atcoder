from functools import lru_cache
@lru_cache()
def gcd(x,y):
    r = x%y
    if r == 0:
        return y
    return gcd(y,r)

K = int(input())
Sum = 0

for i in range(1,K+1):
    Sum += i
    for j in range(i+1,K+1):
        Sum += 6*gcd(i,j)
        for k in range(j+1,K+1):
            Sum += 6*gcd(gcd(i,j),k)
print(Sum)