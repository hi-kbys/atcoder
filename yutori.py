import sys 
args = sys.argv
print(args)
N, K, C = map(int,sys.stdin.readline().split())
S = [i for i in sys.stdin.readline()]
l = [i+1 for i in range(N) if S[i] == 'o']
forward = []
backwardv= []
for u in l:
    if forward == []:
        forward += [u]
    else:
        if u > forward[-1]+C:
            forward += [u]