def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    a,b,c = map(int, input().split())
    import numpy as np
    if c-a-b >=0 and (c-a-b)**2-4*a*b > 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()