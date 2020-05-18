def main():
    import sys
    input = sys.stdin.buffer.readline
    a,b,h,m = map(int, input().split())
    import numpy as np
    theta1 = np.pi*(h/6+m/360)
    theta2 = np.pi*m/30

    theta = min(abs(theta1-theta2), 2*np.pi-abs(theta1-theta2))
    c = np.sqrt(a**2 + b**2 - 2*a*b*np.cos(theta))
    print(c)


if __name__ == '__main__':
    main()