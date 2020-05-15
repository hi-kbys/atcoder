# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import numpy as np
H,W,N = map(int,input().split())
h_arr = [0]*N
w_arr = [0]*N
x_arr = [0]*N
field = np.zeros(H*W).reshape(H,W)
#print(field)
for i in range(N):
    h,w,x = map(int, input().split())
    h_arr[i],w_arr[i],x_arr[i] = h,w,x

for i in range(N):
    check = False
    h,w,x = h_arr[i],w_arr[i],x_arr[i]
    for j in range(H):
        if sum(field[j,x:x+w]) > 0:
            check = True
            field[j-h:j,x:x+w] = np.ones(h*w).reshape(h,w)
            break
        if j == H-1 and sum(field[j,x:x+w]) == 0:
            field[j-h+1:,x:x+w] = np.ones(h*w).reshape(h,w)
for l in field:
    s = ['#' if i == 1 else '.' for i in l ]
    print(''.join(s))
            