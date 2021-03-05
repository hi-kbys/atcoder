def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    for i in range(1000):
        if (n+ i)%1000 == 0:
            print(i)


if __name__ == '__main__':
    main()