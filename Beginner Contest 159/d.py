def nc2(n):
    return int(n*(n-1)/2)


def main():
    import sys
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    from collections import Counter as cc
    a_ = cc(a)
    sum_ = sum([nc2(k) for k in a_.values() if k > 1])
    for i in range(n):
        if a_[a[i]] < 2:
            print(sum_)
        else:
            print(sum_ - (a_[a[i]] -1))


if __name__ == '__main__':
    main()