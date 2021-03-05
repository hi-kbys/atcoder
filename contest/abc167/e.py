mod = 10**9 + 7
mod = 998244353
class mint:

    def __init__(self, x=0):
        self.x = x.x if isinstance(x, mint) else x % mod

    __str__ = lambda self:str(self.x)
    __repr__ = __str__
    __int__ = lambda self: self.x
    __index__ = __int__

    __add__ = lambda self, other: mint(self.x + mint(other).x)
    __sub__ = lambda self, other: mint(self.x - mint(other).x)
    __mul__ = lambda self, other: mint(self.x * mint(other).x)
    __pow__ = lambda self, other: mint(pow(self.x, mint(other).x, mod))
    
    def inv(self):
        return mint(pow(self.x, mod-2, mod))

    __truediv__ = lambda self, other: mint(self.x * mint(other).inv())
    __floordiv__ = lambda self, other: mint(self.x // mint(other).x)
    __radd__ = lambda self, other: mint(other + self.x)
    __rsub__ = lambda self, other: mint(other - self.x)
    __rpow__ = lambda self, other: mint(pow(other, self.x, mod))
    __rmul__ = lambda self, other: mint(other * self.x)
    __rtruediv__ = lambda self, other: mint(other * mint(other).inv())
    __rfloordiv__ = lambda self, other: mint(other // self.x)

    __lt__ = lambda self, other: self.x < mint(other).x
    __gt__ = lambda self, other: self.x > mint(other).x
    __le__ = lambda self, other: self.x <= mint(other).x
    __ge__ = lambda self, other: self.x >= mint(other).x
    __eq__ = lambda self, other: self.x == mint(other).x
    __ne__ = lambda self, other: self.x != mint(other).x


class Combination():
    def __init__(self, n, mod=10**9+7):
        self.mod = mod
        self.fact = [mint(1)]*(n+1)
        self.ifact = [mint(1)]*(n+1)
        for i in range(1, n+1):
            self.fact[i] = self.fact[i-1] * i
        self.ifact[-1] = self.fact[-1].inv()
        for i in range(n-1, 0, -1):
            self.ifact[i] = self.ifact[i+1] * (i+1)
    
    def combination(self, n, r):
        ret = self.fact[n] * self.ifact[r] * self.ifact[n-r]
        if ret >= r:
            return ret
        else:
            return 0
    
def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, m, k = map(int, input().split())
    mod = 998244353
    c = Combination(n)
    ans = mint()
    mex = [mint()]*(k+1)
    mex[0] = (m-1)**(n-k-1)
    # inv(m-1)だとおそらく計算誤差が生じる。
    for i in range(1,k+1):
        mex[i] = mex[i-1]*(m-1)
    mex = mex[::-1]
    for i in range(k+1):
        ans += c.combination(n-1, i)*mex[i]
    ans *= m
    print(ans)


if __name__ == '__main__':
    main()