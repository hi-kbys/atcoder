def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    h, w, K = map(int, input().split())
    field = []
    base = 0
    for i in range(h): 
        s = input()
        s = [1 if _ == '#' else 0 for _ in s]
        field.append(s)
        base += sum(s)
    ans = 0  
    for i in range(2**h):
        for j in range(2**w):
            num = base
            for k in range(h):
                if (i >> k) & 1:
                    num -= sum(field[k])
                else:
                    for l in range(w):
                        if (j >> l) & 1 and field[k][l]:
                            num -= 1
        
            if num == K:
                ans += 1
    print(ans)

            

if __name__ == '__main__':
    main()