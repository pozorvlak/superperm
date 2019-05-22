import sys


def recycle_sequence(n):
    a = [0 for i in range(n)]
    f = list(range(1, n+1))
    while f[0] < n:
        j = f[0]
        f[0] = 1
        ib = 1 if a[j-1] <= 1 else 0
        yield(n - (j + ib % 2))
        a[j-1] += 1
        f[j-1] = f[j]
        f[j] = j + 1
    yield(n - (n % 2))
    f[0] = 1


def reuse(n, r):
    for i in range(1, n):
        yield(n)
    yield(n - r + 1)


def recycle_sequence_reuse(n):
    a = [0 for i in range(n)]
    f = list(range(1, n+1))
    while f[0] < n:
        j = f[0]
        f[0] = 1
        ib = 1 if a[j-1] <= 1 else 0
        for v in reuse(n + 1, n - (j + ib % 2)):
            yield v
        a[j-1] += 1
        f[j-1] = f[j]
        f[j] = j + 1
    for v in reuse(n + 1, n - (n % 2)):
        yield v
    f[0] = 1

n = int(sys.argv[1])
print(list(recycle_sequence_reuse(n)))
