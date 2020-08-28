def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    x = input()
    k = int(x,2)
    c = x.count('1')
    kp = k%(c+1)
    if c > 1:
        kn = k%(c-1)
    
    for i in range(n):
        cnt = 1
        if x[i] == '1':
            if c == 1:
                print(0)
                continue
            mod = c-1
            tmp = (kn - pow(2,n-i-1,mod))%mod
            while 1:
                if tmp == 0:
                    break
                tmp = tmp%format(tmp, 'b').count('1')
                cnt+=1
        else:
            mod = c+1
            tmp = (kp + pow(2,n-i-1,mod))%mod
            while 1:
                if tmp == 0:
                    break
                tmp = tmp%format(tmp, 'b').count('1')
                cnt+=1
        print(cnt)


if __name__ == '__main__':
    main()