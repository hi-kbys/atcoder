def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    l, r , d = map(int, input().split())
    ans = r//d - l//d
    if l%d == 0:
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()