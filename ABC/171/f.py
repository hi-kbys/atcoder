def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    
    k = int(input())
    s = input()
    n = len(s)
    mod = 10**9+7
    p25 = [0]*(k+1)
    p26 = [0]*(k+1)
    c = [0]*(k+1)

    p25[0], p26[0] = 1, 1
    c[0]= 1
    for i in range(1, k+1):
        p25[i] = p25[i-1]*25
        p25[i] %= mod
        p26[i] = p26[i-1]*26
        p26[i] %= mod
        c[i] = (n+i-1)*c[i-1]
        c[i] *= pow(i, mod-2, mod)
        c[i] %= mod
    p25.reverse()
    c.reverse()
    ans = 0
    for i in range(k+1):
        tmp = p25[i]*p26[i]*c[i]
        tmp %= mod
        ans += tmp
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()