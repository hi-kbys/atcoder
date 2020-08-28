def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    def to_int(x): 
        x = int(x)
        if x == -1:
            return x
        else:
            return x-1

    n = int(input())
    p = list(map(to_int, input().split()))
    dic ={}
    for i,node in enumerate(p):
        if [node,i] in dict.values():
            continue
        dic.add([i,node])



    


if __name__ == '__main__':
    main()