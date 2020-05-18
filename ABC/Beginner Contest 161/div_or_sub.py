import collections
def prime_factorize(n):
    a = []
    while n%2 == 0:
        a.append(2)
        n//=2
    f =3
    while f*f <= n:
        if n%f == 0:
            a.append(f)
            n//=f
        else:
            f +=2
    if n != 1:
        a.append(n)
    return a

# N-1の約数を数える
N = int(input())
factor = collections.Counter(prime_factorize(N-1))
K = 1
for i in list(factor.values()):
    K *= i+1
K -=1
for f in range(2, int(N**0.5)+1):
    n = N
    if n%f != 0:
        continue
    while n%f ==0:
        n//=f
    if n%f ==1 or n==1:
        K+=1
#最後は自分自身を加える。
K +=1
print(K)