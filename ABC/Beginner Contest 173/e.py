def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mod = 10 ** 9+ 7
    ans = 1
    a.sort(reverse=True,key= lambda x: abs(x))
    for i in range(k):
        ans *= a[i]
    if base < 0:
        while i > 0:
            if a[i] < 0:

    print(ans)
    exit(0)
    
 

if __name__ == '__main__':
    main()