def main():
    import sys
    
    def input(): return sys.stdin.readline().rstrip()
    
    def make_divisors(n):
        lower_divisors, upper_divisors = [], []
        i = 1
        while i*i <= n:
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n//i)
            i += 1
        return lower_divisors + upper_divisors[::-1]

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

    n = int(input())
    arr = make_divisors(n)
    ans = 0
    for a in arr:
        if n//a%a ==1:
            ans += 1
    arr2 = factorization(n-1)
    tmp = 1
    for a in arr2:
        tmp *= a[1]+1
    ans += tmp
    ans -=1
    print(ans)





if __name__ == '__main__':
    main()