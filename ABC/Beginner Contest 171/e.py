def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    A = list(map(int, input().split()))
    s = 0
    for a in A:
        s = s^a
    B = [s^a for a in A]
    print(*B)



if __name__ == '__main__':
    main()