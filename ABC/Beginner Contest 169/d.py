
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def main():
    import numpy as np
    import sys
    n = int(input())
    arr = factorization(n)
    ans = 0
    for fact,num in arr:
        if fact == 1:
            print(0)
            exit(0)
        ans += int((np.sqrt(1+8*num) - 1)/2)  
    print(ans)


if __name__ == '__main__':
    main()