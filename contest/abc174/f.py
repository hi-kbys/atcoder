class FenwickTree():
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)
    
    def sum(self, i):
        '''
        i: 1-indexed
        bit(i)のうち最後に現れる1をi -= i&(-i)で消している。
        '''
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def add(self, i, x):
        '''
        i: 1-indexed
        '''
        while i <= self.n:
            self.tree[i] += x
            i += i & -i
    
    def query(self, l, r):
        '''
        区間[l, r]でのsumを返す。
        l, r 1-indexed
        '''
        return self.sum(r)-self.sum(l-1)

def main():
    import sys
    from collections import defaultdict

    def input(): return sys.stdin.readline().rstrip()
    
    n, q = map(int, input().split())
    c = [0]+list(map(int, input().split()))
    que = defaultdict(lambda: [])
    cset = defaultdict(int)
    for i in range(q):
        l, r = map(int, input().split())
        que[r].append((l, i))
    # que.sort(key=lambda x: x[2])
    ans = [0]*q
    ft = FenwickTree(n)
    for i in range(1, n+1):
        if cset[c[i]] > 0:
            ft.add(cset[c[i]], -1)
        ft.add(i, 1)
        cset[c[i]] = ic
        for l, k in que[i]:
            ans[k] = ft.query(l, i)
    for x in ans:
        print(x)



if __name__ == '__main__':
    main()