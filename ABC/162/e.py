def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, k = map(int, input().split())
    mod = 10 ** 9+ 7
    table = [0]*(k+1)
    ans= 0
    for i in range(k, 0, -1):
        table[i] = pow(k//i, n, mod)
        j = 2
        while i*j <= k:
            table[i] -= table[i*j]
            table[i] %= mod
            j += 1
        ans += i*table[i]
        ans %= mod
    print(ans)



if __name__ == '__main__':
    main()