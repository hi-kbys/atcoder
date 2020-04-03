N, X, Y= map(int, input().split())
K = [0]*(N-1)
for i in range(1,N):
    for j in range(i+1, N+1):
        idx = min([j-i, abs(X-i)+ abs(j-Y)+1, abs(Y-i) + 1 + abs(X-j)])-1
        K[idx] +=1
for value in K:
    print(value)    