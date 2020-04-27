import sys
N = int(input())
r3 = N//3
r5 = N//5
r15 = N//15
def sum(N):
    return int(1/2*N*(N+1))
S = sum(N) - 3*sum(r3) - 5*sum(r5) +15*sum(r15)
print(S)