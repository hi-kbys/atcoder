N = int(input())
S= input()
sub = 0
R,G,B = [],[],[]
r = S.count('R')
g = S.count('G')
b = S.count('B') 
for i in range(N):
    for j in range(i+1,N):
        if 2*j-i > N-1:
            break
        if S[i] != S[j] and S[2*j-i] != S[i] and S[2*j-i] != S[j]:
            sub += 1
ans = r*g*b -sub
print(ans)