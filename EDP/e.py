def main():
    import sys
    input = lambda: sys.stdin.buffer.readline().rstrip()
    n, w = map(int, input().split())
    import numpy as np

    dp = np.zeros((n+1, w+1), dtype=int)
    
    for i in range(n):
        v,w


if __name__ == '__main__':
    main()