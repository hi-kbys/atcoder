def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n , k = map(int, input().split())
    a = list(map(int, input().split()))
    
    def check(m):
        cnt = 0
        for x in a:
            cnt += (x-1)//m
        return cnt <= k

    l, r = 0, max(a)
    # めぐる式にぶたん
    while r-l > 1:
        m = (r+l)//2
        if check(m): r = m
        else: l = m
    print(r)

    


if __name__ == '__main__':
    main()