def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    x,n = map(int, input().split())
    p = list(map(int, input().split()))
    l = [abs(i-x) if i not in p else 103 for i in range(102)]

    ans = l.index(min(l))
    print(ans)
    
if __name__ == '__main__':
    main()
