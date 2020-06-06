def main():
    import sys
    n = int(input())
    A,B = [],[]
    for i in range(n):
        a,b= map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(A)
    B = sorted(B)
    if n%2 == 0:
        ma = (A[n//2]+A[n//2-1])/2
        mb = (B[n//2]+B[n//2-1])/2
        ans = int(2*(mb-ma) + 1)
        print(ans)
    else:
        ma = A[n//2]
        mb = B[n//2]
        ans = (mb-ma) + 1
        print(ans)
        
        
if __name__ == '__main__':
    main()