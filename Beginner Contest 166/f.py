N,A,B,C = map(int,input().split())
s = []
for _ in range(N):
    s.append(input())
from collections import Counter as cc
s_ = cc(s)
ans = 'Yes'

if s_['AB'] > s_['BC'] + s_['CA']:
    ans = 'No'
    print(ans)
    exit(0)
if s_['BC'] > s_['AB'] + s_['CA']:
    ans = 'No'
    print(ans)
    exit(0)
if s_['CA'] > s_['BC'] + s_['AB']:
    ans = 'No'
    print(ans)
    exit(0)
