#!/usr/bin/env python
import sys


def recycle_sequence(n):
    global a, f
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
    global a, f
    for i in range(1, n):
        yield(n)
    yield(n - r + 1)


def recycle_sequence_reuse(n):
    global a, f
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


def rewind(n, m, seq):
    for v in seq(n-1):
        yield v
    yield n-1
    yield n
    for i in range(1, m-1):
        for v in seq(n-1):
            yield n
    for v in seq(n-1):
        yield v
    yield n-1
    yield n


def rotate(perm, i):
    return perm[1:i] + [perm[0]] + perm[i:]


n = int(sys.argv[1])
a = [0 for i in range(n)]
f = list(range(1, n+1))
for i in range(n):
    rsr = list(rewind(n, i, recycle_sequence_reuse))
    print(rsr)
    print(len(rsr))
    p = list(range(1, n+1))
    print(p)
    for r in rsr:
        p = rotate(p, r)
        print(p)

