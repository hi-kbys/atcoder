def main():
    import sys
    input = sys.stdin.buffer.readline
    from collections import Counter as cc
    from fractions import gcd
    n = int(input())
    mod = 10**9 + 7
    C_p,C_n = cc(),cc()
    count= 0
    count_zero_a = count_zero_b = 0
    ans = 1
    for i in range(n):
        a,b = map(int, input().split())
        if a == 0 and b == 0:
            count += 1
        else:
            gcd_ab = gcd(a,b)
            a //= gcd_ab
            b //= gcd_ab
            if b == 0:
                count_zero_b += 1
            elif a == 0: 
                count_zero_a += 1
            else:
                if a/b>0:
                    C_p[a,b] += 1
                else:
                    C_n[a,b] += 1
    count_zero = count
    ans *= (2**count_zero_a + 2**count_zero_b -1)%mod
    count += count_zero_a + count_zero_b    
    for a,b in C_p:
        if (-b,a) in C_n:
            count += C_n[-b,a] + C_p[a,b]
            ans *= (2**C_n[-b,a] + 2**C_p[a,b] -1)%mod
    ans *= pow(2, n-count,m od)%mod
    ans = (ans + count_zero - 1) % mod
    print(ans)


if __name__ == '__main__':
    main()