def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    
    n = int(input())
    c = input()

    s = 0
    e = n-1
    cnt = 0
    while s < e:
        while c[s] != 'W' and s < e:
            s+= 1
        
        while c[e] != 'R' and s < e:
            e -= 1
        if c[e] != c[s]:
            cnt += 1
        s+= 1
        e -= 1
    print(cnt)

        

if __name__ == '__main__':
    main()