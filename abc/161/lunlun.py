def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    k = int(input())
    from collections import deque
    que = deque(range(1, 10))
    for i in range(k):
        now = que.popleft()
        r = now%10
        nx = now*10
        if r == 0:
            for j in [0, 1]:
                que.append(nx+r+j)
        elif r == 9:
            for j in [-1, 0]:
                que.append(nx+r+j)
        else:
            for j in [-1, 0, 1]:
                que.append(nx+r+j)
    print(now)

if __name__ == '__main__':
    main()