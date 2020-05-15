# 階乗の計算をmodで割る
class mod_comb():
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1]*(n+1)
        for i in range(1,n+1):
            self.fac[i] = self.fac[i-1] * i % self.mod
        self.invfac = [1]*(n+1)
        self.invfac[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n-1, 0, -1):
            self.invfac[i] = self.invfac[i+1] * (i+1) % self.mod
    
    def combination(self, n, r):
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n-r] % self.mod


# 01での全探索
def bit_search(N):
    for i in range(2**N):
        for j in range(N):
            # bit 演算！j桁ずらしている。
            if ((i >> j) & 1) == 1:
                # task