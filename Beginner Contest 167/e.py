class mod_comb():
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1]*(n+1)
        for i in range(1,n+1):
            self.fac[i] = self.fac[i-1] * i % self.mod
        self.invfac = [1]*(n+1)
        self.invfac[n] = pow(self.fac[n], self.mod - 2, self.mod) # modが素数なら逆元になる
        for i in range(n-1, 0, -1):
            self.invfac[i] = self.invfac[i+1] * (i+1) % self.mod
    
    def combination(self, n, r):
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n-r] % self.mod


def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M, K = map(int, input().split())
    mod = 998244353
    comb = mod_comb(N, mod)
    ans = 0
    for i in range(K+1):
        ans = comb.combination(N-1, K)


if __name__ == '__main__':
    main()