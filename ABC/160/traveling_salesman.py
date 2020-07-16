import numpy as np
K, N = map(int, input().split())
A = list(map(int, input().split()))
diff = np.diff(A)
diff = np.append(diff, A[0] + K - A[-1])
minimum = K - max(diff)
print(minimum)

