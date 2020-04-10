import sys
def yutori():
    N, K, C = map(int,sys.stdin.readline().split())
    S = [i for i in sys.stdin.readline()]
    l = [i+1 for i in range(N) if S[i] == 'o']
    Left = [0]*K
    Right = [0]*K
    count = 0
    for u in l:
        if Left[0] == 0:
            Left[count] = u
        if u > Left[count] + C:
            count +=1
            Left[count] = u
        continue

    count = 1
    for u in l[::-1]:
        if Right[-1] == 0:
            Right[-count] = u
        if u < Right[-count] - C:
            count +=1
            Right[-count] = u
        continue

    if Left[-1] == 0 or Right [0] == 0:
        return 
    for i in range(K):
        if Left[i] == Right[i]:
            print(Left[i])

yutori()
