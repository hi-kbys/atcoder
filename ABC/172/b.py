def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    S = input()
    T = input()
    count = 0
    for s,t in zip(S,T):
        if s != t:
            count += 1
    print(count)


if __name__ == '__main__':
    main()