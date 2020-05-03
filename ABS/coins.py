# import sys 
# import os
# import numpy as np

# path = os.path.join(os.getcwd(),'input.txt')
# input = open(path).readline

A,B,C,X = [int(input()) for _ in range(4)]

count = 0
A = min(A,X//500)
B = min(B,X//100)
C = min(C,X//50)
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if X == 500*a + 100*b+ 50*c:
                count +=1
print(count)