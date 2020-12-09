import sys

def find_sum(l, total):
    for i in l:
        m = list(filter(lambda x: i + x == total, l))
        if m:
            return (i, m[0])
    return (None, None)

ns = []
with open("input") as f:
    for n in f:
        n=int(n)
        n1, n2 = find_sum(ns, 2020-n)
        if n1:
            print(n1*n2*n)
            sys.exit(0)
        ns.append(n)
