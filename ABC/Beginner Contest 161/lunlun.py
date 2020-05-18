import queue
K = int(input())
q = queue.Queue()
for i in range(1,10):
    q.put(i)

for i in range(K):
    x = q.get()
    a = x%10
    if a !=0:
        q.put(10*x +a -1)
    q.put(10*x +a )
    if a != 9:
        q.put(10*x +a +1)
print(x)