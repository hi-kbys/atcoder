import sys

input = sys.stdin.readline

X = int(input())
year = 0
N = 100
while N < X:
    N = int(1.01*N)
    year +=1
print(year)