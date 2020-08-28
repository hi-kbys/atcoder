A,B,C,K = map(int,input().split())

if K-A <= 0 :
    ans = K
else:
    ans = A
    if K-A-B <= 0:
        pass
    else:
        ans -= (K-A-B)
print(ans)

