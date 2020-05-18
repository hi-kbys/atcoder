def main():
    import sys
    input = sys.stdin.buffer.readline
    h,w,k = map(int, input().split())
    import numpy as np
    a = np.zeros((h,w), dtype=int)
    for i in range(h):
        a[i] = list(map(int, input().split()))
    
    for i in range(2**(h-1)):
        for j in range(h):
            if ((i >> j)&1) == 1:



if __name__ == '__main__':
    main()