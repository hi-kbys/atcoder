def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    ans = [0]*(n+1)
    lim = int(n**(0.5)) +1
    for i in range(1, lim):
        for j in range(1,lim):
            for k in range(1,lim): 
                tmp = i**2 + j**2 + k**2 +i*j + j*k+ k*i
                if tmp <= n:
                    ans[tmp] += 1
    for a in ans[1:]:
        print(a)   


if __name__ == '__main__':
    main()