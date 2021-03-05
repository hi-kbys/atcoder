def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(0, n, 2):
        if a[i]%2 == 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()