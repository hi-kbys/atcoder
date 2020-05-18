def main():
    import sys
    input = sys.stdin.buffer.readline
    n = int(input())
    if (m:= n%10) in [2,4,5,7,9]:
        print('hon')
    elif m in [0,1,6,8]:
        print('pon')
    elif m == 3:
        print('bon')


if __name__ == '__main__':
    main()