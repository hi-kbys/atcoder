def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    a = int(input())
    ans = 0
    for i in range(3):
        ans += a**(i+1)
    print(ans)


if __name__ == '__main__':
    main()