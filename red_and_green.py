X,Y,A,B,C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)
P = P[:X]
Q = Q[:Y]
All = P + Q + R
All.sort(reverse = True)
print(sum(All[:X+Y]))