import sys

x = int(input())
happiness = 0
happiness += x//500 * 1000
x = x%500
happiness += x//5 * 5
print(happiness)
