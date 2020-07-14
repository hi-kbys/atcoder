def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    height = [0]*n
    for i in range(m):
        a, b = map(lambda x: int(x)-1, input().split())
        height[a] = max(height[a], h[b])
        height[b] = max(height[b], h[a])
    
    count = 0
    for i, j in zip(h, height):
        if i > j:
            count += 1
    print(count)

if __name__ == '__main__':
    main()