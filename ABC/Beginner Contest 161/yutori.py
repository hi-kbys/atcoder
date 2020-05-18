import sys
def yutori():
    N, K, C = map(int,sys.stdin.readline().split())
    S = [i for i in sys.stdin.readline()]
    l = [i+1 for i in range(N) if S[i] == 'o']
    Left = []
    Right = []
    for u in l:
        if Left == []:
            Left.append(u)
        if u > Left[-1] + C:
            Left.append(u)
        if len(Left) == K:
            break

    if len(Left) <K:
        exit()

    for u in l[::-1]:
        if Right== []:
            Right.append(u)
        if u < Right[-1] - C:
            Right.append(u)
        if len(Right) == K:
            break

    if len(Right) <K:
            exit()
    
    for i in range(K):
        if Left[i] == Right[-i-1]:
            print(Left[i])

yutori()
