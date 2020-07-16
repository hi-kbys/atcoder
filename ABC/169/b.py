def main():
    import sys
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    limit = 10**18
    ans = 1
    for ai in a:
        ans *= ai
        if ans > limit:
            print(-1)
            exit(0)
        if ans == 0:
            break
    print(ans)

    


if __name__ == '__main__':
    main()