import sys

input = sys.stdin.readline
ans = 'NG'
N = int(input())
A,B = map(int,input().split())
for i in range(A,B+1):
    if i%N == 0:
        ans = 'OK'
print(ans)