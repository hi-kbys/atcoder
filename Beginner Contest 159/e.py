def main():
    import sys
    input = sys.stdin.buffer.readline
    h,w,k = map(int, input().split())
    import numpy as np
    a = np.zeros((h,w), dtype=int)
    for i in range(h):
        a[i] = list(map(int, input().split()))
    


if __name__ == '__main__':
    main()