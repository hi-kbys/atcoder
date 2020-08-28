from collections import deque
from heapq import heappop, heappush


# 階乗の計算をmodで割る
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
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n-r] % self.mod

    def permutation(self, n, r):
        return self.factorial(n) * self.invfactorial(n-r) % self.mod

    def factorial(self, i):
        return self.fac[i]

    def invfactorial(self, i):
        return self.invfac[i]


# 全方位木dp, 適宜計算用のクラスを継承して使用する。
class Rerooting():
    def __init__(self, adjacent):
        # super(Rerooting, self).__init__(n, mod)
        self.n = n
        self.adj = adjacent   # 0-indexedの配列で用意！
        # DFSで行きがけ順を記録
        self.order = []
        stack = [0]
        self.parent = [-1]*(n)
        while stack:
            node = stack.pop()
            self.order.append(node)
            for child in self.adj[node]:
                if self.parent[node] == child:
                    continue
                stack.append(child)
                self.parent[child] = node
    
    def merge(self, parent, child):
        # childの値をparentに統合する処理
        return self.dp[parent]

    def remerge(self, parent, child):
        # childの値が根となるときの統合処理
        return self.dp[child]

    def calc_subtree(self):
        # 帰りがけ順で木DPを行う
        # 根が0の時の値を算出
        self.dp = [1]*(self.n)
        self.size = [1]*(self.n)
        for node in self.order[::-1]:
            if self.parent[node] == -1:
                continue
            self.merge(self.parent[node], node)

    def root_subtree(self):
        # 行きがけ順で根を更新する。
        for node in self.order[1:]:
            p = self.parent[node]
            self.remerge(p, node)
        return self.dp


def bit_search(N):
    # 01での全探索
    for i in range(2**N):
        for j in range(N):
            # bit 演算！j桁ずらしている。
            if ((i >> j) & 1) == 1:
                # task


# 深さ優先探索
def DFS(adj):
    stack = [0]
    parent = [-1] * (n)
    while stack:
        node = stack.pop()
        for child in adj[node]:
            if parent[node] == child:
                continue
            stack.append(child)
            parent[child] = node
    return -1

# 幅優先探索
def BFS(adj):
    que = deque([0])
        parent = [-1] * (n)
        while que:
            node = que.popleft()
            for child in adj[node]:
                if parent[node] == child:
                    continue
                if parent[child] == -1:
                    que.append(child)
                    parent[child] = node
    return -1

def gcd(x,y):
    r = x%y
    if r==0:
        return y
    return gcd(y, r)

def modinv(a,p):
    return pow(a, p-2, p)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# dfsの重複組み合わせバージョン
def dfs(n,m):
    adj = {}
    for i in range(1,m+1):
        adj[i] = [j for j in range(i,m+1)]
    
    stack = [[i] for i in range(1,m+1)]
    combs = []
    while stack:
        node = stack.pop()
        if len(node) == n:
            combs.append(node)
        else:
            for child in adj[node[-1]]:
                cand = node+[child]
                stack.append(cand)
    return combs

# Union Find木クラス
class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0]*n

    def get_root(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]
        
    def unite(self, i, j):
        root_i = self.get_root(i)
        root_j = self.get_root(j)
        if root_i != root_j:
            if self.height[root_i] < self.height[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.height[root_i] == self.height[root_j]:
                    self.height[root_i] += 1
    
    def is_in_group(self, i, j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False


def kruskal(n, edge_list):
    '''
    edge_list: [edge0, edge1, cost]
    '''
    edge_list.sort(key=lambda x: x[2])
    uf_tree = UnionFind(n)
    mst = []
    cost = 0
    for edge in edge_list:
        if not uf_tree.is_in_group(edge[0], edge[1]):
            uf_tree.unite(edge[0], edge[1])
            mst.append(edge[:2])
            cost += edge[2]
    return mst, cost


def prim(n, e_list):
    '''
    e_list = [from, to, cost]
    '''
    edges_from = [[] for i in range(n)]
    for e in e_list:
        edges_from[e[0]].append([e[2], e[0], e[1]])
        edges_from[e[1]].append([e[2], e[1], e[0]])
    e_heapq = []
    included = [False]*n
    mst = []
    cost = 0
    included[0] = True
    for e in edges_from[0]:
        heappush(e_heapq, e)
    while e_heapq:
        # print(e_heapq)
        c, *e = heappop(e_heapq)
        if not included[e[1]]:
            included[e[1]] = True
            mst.append(e)
            cost += c
            for child in edges_from[e[1]]:
                heappush(e_heapq, child)
    mst.sort()
    return mst, cost


def dijkstra(s, e_list):
    inf = 1 << 18
    n = len(e_list)
    dist = [inf]*(n)
    dist[s] = 0
    que = [(0, s)]
    while que:
        node, cost = heappop(que)
        if cost > dist[node]:
            continue
        for v in e_list[node]:
            if dist[v] > dist[node]+1:
                dist[v] = dist[node]+1
                heappush(que, (dist[v], v)) 
    return dist

class SegTree():
    inf = 1 << 18
    def __init__(self, arr, segfunc=min, ide_ele=inf):
        '''
        arr: 与えられた配列
        segfunc: 区間に作用する関数
        ide_ele: 単位元
        num: n を超える初めの2の累乗
        tree: size = 2*num のセグ木
        計算量O(2n)
        '''
        n = len(arr)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [self.ide_ele]*2*num
        for i in range(n):
            self.tree[i+self.num] = arr[i]
        for i in range(self.num-1, -1, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
        
    def update(self, k, x):
        '''
        k : index
        x : update value
        '''
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k>>1] = self.segfunc(self.tree[k], self.tree[k^1])
            k >>= 1
    
    def query(self, l, r)
        '''
        区間[l, r)でsegfuncしたものを得る
        '''
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            res = self.ide_ele
            if l & 1:
                res = self.segfunc(res, self.tree[l])
            if r&1:
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

class FenwickTree():
    def __init__(self, n):
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
        while i <= n:
            self.tree[i] += x
            i += i % -i
    
    def query(self, l, r):
        '''
        区間[l, r]でのsumを返す。
        l, r 1-indexed
        '''
        return sum(r)-sum(l-1)
