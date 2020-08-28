def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    a = input()
    if a.upper() == a:
        print('A')
    else:
        print('a')


if __name__ == '__main__':
    main()