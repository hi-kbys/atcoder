def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n,m = map(int, input().split())
    if n%2 == 0:
        for i in range(m):
            print(n//2-i, n//2+i+1)
    else:
        for i in range(m):
            print(n//2-i, n//2+i+2)



if __name__ == '__main__':
    main()