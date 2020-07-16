def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    from collections import Counter as cc
    S = []
    for i in range(n):
        S.append(input())
    S = cc(S)
    print('AC x {}'.format(S['AC']))
    print('WA x {}'.format(S['WA']))
    print('TLE x {}'.format(S['TLE']))
    print('RE x {}'.format(S['RE']))


if __name__ == '__main__':
    main()