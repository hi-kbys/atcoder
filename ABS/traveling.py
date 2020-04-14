N = int(input())
T = []
X = []
Y = []
for i in range(N):
    t,x,y = map(int,input().split())
    T.append(t)
    X.append(x)
    Y.append(y)
for i in range(N):
    if i == 0:
        t,x,y = T[i],X[i],Y[i]
    else:
        t = T[i]-T[i-1]
        x = X[i]-X[i-1]
        y = Y[i]-Y[i-1]
    if t%2 == (x+y)%2 and abs(x)+abs(y) <= t:
        if i == N-1:
            print('Yes')
        continue
    else:
        print('No')
        break