def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    T = input()
    T = T.replace('?','D')
    print(T)


if __name__ == '__main__':
    main()