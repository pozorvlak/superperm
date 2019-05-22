import sys

n = int(sys.argv[1])

a = [0 for i in range(n)]
f = list(range(1, n+1))

while f[0] < n:
    j = f[0]
    f[0] = 1
    ib = 1 if a[j-1] <= 1 else 0
    print(n - (j + ib % 2))
    a[j-1] += 1
    f[j-1] = f[j]
    f[j] = j + 1
print(n - (n % 2))
f[0] = 1
