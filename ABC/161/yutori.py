def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, k, c = map(int, input().split())
    s = [True if i == 'o' else False for i in input()]
    L = [0]*k
    R = [0]*k
    # 右から貪欲法
    i = n-1
    now = k-1
    while 0 <= now:
        if s[i]:
            R[now] = i
            i -= c
            now -= 1
        i -= 1
    # 　左から貪欲
    i = 0
    now = 0
    while now < k:
        if s[i]:
            L[now] = i
            # rangeが一致しているなら出力
            if L[now] == R[now]:
                print(i+1)
            i += c
            now += 1
        i += 1

        



if __name__ == '__main__':
    main()