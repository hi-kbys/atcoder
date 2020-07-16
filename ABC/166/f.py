def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    def conv(s):
        ret = []
        for i in s:
            if i == 'A':
                ret.append(0)
            elif i == 'B':
                ret.append(1)
            else:
                ret.append(2)
        return ret

    def inv(i):
        if i == 0:
            return 'A'
        elif i == 1:
            return 'B'
        else:
            return 'C'

    def answer(ans):
        print('Yes')
        for a in ans:
            print(a)
        return -1

    def add_answer(x):
        if s[x[0]] > s[x[1]]:
            s[x[0]] -= 1
            s[x[1]] += 1
            ans.append(inv(x[1]))
        else:
            s[x[0]] += 1
            s[x[1]] -= 1
            ans.append(inv(x[0]))
        
    n, *s = map(int, input().split())
    idx_list = []
    for i in range(n):
        idx_list.append(conv(input()))

    ans = []
    if sum(s) == 0:
        print('No')
        exit(0)

    elif sum(s) == 1:
        for x in idx_list:
            if s[x[0]] == s[x[1]]:
                print('No')
                exit(0)
            add_answer(x)
        answer(ans)

    else:
        for i, x in enumerate(idx_list):
            if s[x[0]] == 0 and s[x[1]] == 0:
                print('No')
                exit(0)
                
            if i < n-1 and s[x[0]] == 1 and s[x[1]] == 1:
                nx = idx_list[i+1]
                if x != nx:
                    if x[0] in nx:
                        s[x[0]] += 1
                        s[x[1]] -= 1
                        ans.append(inv(x[0]))
                    else:
                        s[x[0]] -= 1
                        s[x[1]] += 1
                        ans.append(inv(x[1]))
            else:
                add_answer(x)
        answer(ans)


if __name__ == '__main__':
    main()
