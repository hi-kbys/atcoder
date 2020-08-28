def main():
    import sys
    input = sys.stdin.buffer.readline
    h1,m1,h2,m2,k = map(int, input().split())
    rem = h2*60+m2-h1*60-m1
    print(rem-k)
    


if __name__ == '__main__':
    main()