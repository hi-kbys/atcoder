def main():
    import sys
    import math
    import numpy as np

    a,b = map(str, input().split())
    a = [int(i) for i in a]
    a += [0]*2
    a = np.array(a)
    b = b.replace('.','')
    b = [int(i) for i in b]
    ans = a*b[0]
    ans[1:] += a[:-1]*b[1]
    ans[2:] += a[:-2]*b[2]
    from functools import reduce
    l = reduce(lambda a,b:10*a+b, ans)
    print(l//100)
    

if __name__ == '__main__':
    main()