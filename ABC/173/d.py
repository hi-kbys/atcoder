def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if n %2== 0:
        print(a[0]+sum(a[1:n//2])*2)
    else:
        print(a[0]+sum(a[1:n//2])*2+a[n//2])



if __name__ == '__main__':
    main()