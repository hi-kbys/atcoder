def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    x, y = map(int, input().split())
    if y%2 == 1:
        print('No')
    elif 2*x-y//2 < 0 or  y//2 - x < 0:
        print('No')
    else:
        print('Yes')
        
    


if __name__ == '__main__':
    main()