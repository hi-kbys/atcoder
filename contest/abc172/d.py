def main():
    '''
    jの倍数の和を順に足してゆけばよい
    '''
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    ans = 0
    sumn = lambda x: x*(x+1)//2
    for i in range(1,n+1):
        r = n//i
        ans += i*(sumn(r))
    print(ans)


if __name__ == '__main__':
    main()