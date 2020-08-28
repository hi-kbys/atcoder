def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    x = list(map(int, input().split()))
    for i,el in enumerate(x):
        if el == 0:
            print(i+1)


if __name__ == '__main__':
    main()