def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    count = 1
    k,l = 26,26
    while k < n:
        l *= 26
        k += l
        count += 1
    r = n - k + l -1
    s = ''
    for i in range(count):
        m = r%26
        r //= 26
        s += chr(ord('a')+ m)
    s = s[::-1]
    print(s)

if __name__ == '__main__':
    main()