import math
from functools import lru_cache

def memoize(func):
    table = {}
    def add_table(*args):
        if not args in table:
            table[args] = func(*args)
        return table[args]
    return add_table

@lru_cache
def size(root, parent):
    Ad =  Adjascent[root]
    if parent != -1:
        Ad = Ad.remove(parent)
    size=1
    if Ad == []:
        return size 
    else: 
        for child in Ad:
            size += get_size(child,root)
    return size
    Ad =  Adjascent[root]

@lru_cache
def dp(root,parent):
    if parent != -1:
        Ad = Ad.remove(parent)
    if Ad == []:
        ret = 1
    else:
        for child in Ad:
            coef = math.factorial(size(root)-1)
            ret = math.factorial(get_size(v)-1)
            ret *= dp_with_parent(u,root)/math.factorial(get_size(u,root))
    return int(ret)   

if __name__ == "__main__":
    N = int(input())
    Adjascent = {}
    for i in range(1,N):
        a,b = map(int, input().split())
        if not a in Adjascent:
            Adjascent[a] = []
        if not b in Adjascent: 
            Adjascent[b] = []
        Adjascent[a].append(b)
        Adjascent[b].append(a)
    for i in range(N)
        print(dp(i+1,-1))