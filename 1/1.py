import sys

ns = []
with open("input") as f:
    for n in f:
        n=int(n)
        m = list(filter(lambda x: n + x == 2020, ns))
        if m:
            print(m[0]*n)
            sys.exit(0)
        ns.append(n)
