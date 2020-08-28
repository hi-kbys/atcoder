def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    k = int(input())

    k *= 9
    if k%7 == 0:
        k //= 7
    tmp = 1
    cnt = 0
    while i < k:
        tmp %= k
        tmp *= 10
        tmp %= k
        cnt += 1


    # tmp = 7
    # cnt = 0
    # if k%2 == 0 or k%5 == 0:
    #     print(-1)
    #     return

    # while 1:
    #     tmp %= k
    #     cnt += 1
    #     if tmp == 0:
    #         break
    #     tmp = 10*tmp%k
    #     tmp += 7
    print(cnt)



if __name__ == '__main__':
    main()