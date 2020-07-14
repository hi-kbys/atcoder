def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    import numpy as np
    A.sort()
    ans = sum(A)
    from bisect import bisect_left,bisect_right
    from collections import Counter
    count = Counter(A)
    for i in range(q):
        b,c = map(int, input().split())
        k = count[b]
        if k != 0:
            count[c] += count.pop(b)
        ans += (c-b)* k
        print(ans)


if __name__ == '__main__':
    main()