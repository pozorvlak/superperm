#!/usr/bin/env python
import sys

# Implementation of the algorithms from the paper "Hamilton Cycles in
# Restricted and Incomplete Rotator Graphs" by Brett Stevens and Aaron
# Williams,
# https://www.researchgate.net/profile/Aaron_Williams10/publication/265584435_Hamilton_Cycles_in_Restricted_and_Incomplete_Rotator_Graphs/links/56d3c2cf08ae85c8234c762b/Hamilton-Cycles-in-Restricted-and-Incomplete-Rotator-Graphs.pdf?origin=publication_detail


def recycle_sequence(n):
    global a, f
    while f[0] < n:
        j = f[0]
        f[0] = 1
        ib = 1 if a[j-1] <= 1 else 0
        yield(n - ((j + ib) % 2))
        a[j-1] += 1
        if a[j-1] == n - j:
            a[j-1] = 0
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
        for v in reuse(n + 1, n - ((j + ib) % 2)):
            yield v
        a[j-1] += 1
        if a[j-1] == n - j:
            a[j-1] = 0
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
    if i == 0:
        return perm
    return perm[1:i] + [perm[0]] + perm[i:]


def list_to_str(perm):
    return "".join(str(p) for p in perm)


n = int(sys.argv[1])
a = [0 for i in range(n)]
f = list(range(1, n+1))
perm = list(range(1, n+1))
for r in recycle_sequence(n):
    print(list_to_str(perm))
    perm = rotate(perm, r)