import sys
import numpy as np

# import os
# path = os.getcwd()
# path = os.path.join(path,"input.txt")
# sys.stdin = open(path)

input = sys.stdin.readline
N = int(input())
p = [int(input()) for i in range(N)]
p.sort(reverse=True)
p[0] = int(p[0]/2)
print(sum(p))