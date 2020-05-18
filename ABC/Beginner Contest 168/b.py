def main():
    import sys
    #input = sys.stdin.buffer.readline
    k = int(input())
    s = input()
    if len(s) > k:
        s = s[:k] + '...'
    print(s)

if __name__ == '__main__':
    main()