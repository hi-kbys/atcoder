def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    h,w = map(int, input().split())
    n = h*w
    if h == 1 or w ==1:
        print(1)
    elif n%2 == 0:
        print(n//2)
    else:
        print(n//2+1)


if __name__ == '__main__':
    main()