def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    
    n, d= map(int, input().split())
    cnt = 0
    for _ in range(n):
        x, y = map(int, input().split())
        
        if x*x+y*y <= d*d:
            cnt += 1
    print(cnt)

        

if __name__ == '__main__':
    main()