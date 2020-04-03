import math

def memoize(func):
    table = {}
    def add_table(*args):
        if not args in table:
            table[args] = func(*args)
        return table[args]
    return add_table

def get_size(root, parent):
    branch = Adjascent[root].remove(parent)
    size = 1
    if len(branch) == 0:
        pass
    else: 
        for e in branch:
            size += get_size(e,root)
    return size

def dp(root):
    ret = []
    return ret
    for child in Adjascent[root]:
        coef = math.factorial(size(root)-1)
        ret.append(dp_with_parent(child,root))
    def dp_with_parent(root, parent):
        upper = [s if s > parent for s in Adjascent[root]]
        lower = [s if s < parent for s in Adjascent[root]]
        if len(branch) == 0:
            ret = 1
        else:
            ret = math.factorial(get_size(v)-1)
            for u in upper.sort(reverse=True):
                ret *= dp_with_parent(u,root)/math.factorial(get_size(u,root))
            for v in lower:
                
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
    
    #print(dp(1))
  