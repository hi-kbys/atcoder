import math
X = int(input())


def fif_root(arg):
    def root(x):
        return math.floor(math.pow(x, 1/5)*pow(10, 10))/pow(10, 10)
    return list(map(lambda x: root(x), arg))

def check_integer(arg):
    return list(map(lambda x: x.is_integer(), arg))

a = 0
while (A:= math.pow(a, 5))-math.pow(a-1, 5) <= X:
    #a,-aの時それぞれの5乗根を計算する。
    root = fif_root([abs(X-A), X+A])
    if True in (c := check_integer(root)):
        idx = c.index(True)
        b = int(root[idx])
        if idx == 1:
            a, b = -a, -b
        else:
            if X - A >= 0:
                b = -b
        print(a, b)
        break
    a += 1

#simple solution

# X = int(input())
# pow5 = [i**5 for i in range(-150,150)]
# for a in range(-150,150):
#   for b in range(-150,150):
#     if pow5[a+150]-pow5[b+150] ==X:
#       print(a,b)
#       exit(0)
