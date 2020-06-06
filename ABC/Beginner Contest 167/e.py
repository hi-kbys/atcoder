class Combination():
    def __init__(self, n, mod=10**9+7):
        self.mod = mod
        self.fac = [1]*(n+1)
        for i in range(1,n+1):
            self.fac[i] = self.fac[i-1] * i % self.mod
        self.invfac = [1]*(n+1)
        self.invfac[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n-1, 0, -1):
            self.invfac[i] = self.invfac[i+1] * (i+1) % self.mod
    
    def combination(self, n, r):
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n-r] % self.mod if n>= r else 0
    
    def factorial(self, i):
        return self.fac[i]
    
    def invfactorial(self, i):
        return self.invfac[i]


def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, m, k = map(int, input().split())
    mod = 998244353
    c = Combination(n,mod)
    ans = 0
    inv = pow(m-1,mod-2,mod)
    rem = pow(m-1, n-1, mod)
    for i in range(k+1):
        ans += c.combination(n-1, i)*rem
        ans %= mod
        rem *= inv
        rem %= mod
    ans *= m
    ans %= mod
    print(ans)


if __name__ == '__main__':
    main()