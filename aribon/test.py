def main():
    import sys
    from collections import deque
    def input(): return sys.stdin.readline().rstrip()
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i = 0
    j = 0
    cnt = 0
    while i < n and j < m:
        while i < n and j < m:
            if a[i]+x <= b[j]:
                cnt += 1
                break
            j += 1
        while j < m and i < n:
            if b[j]+y <= a[i]:
                break
            i += 1
    print(cnt)

if __name__ == '__main__':
    main()