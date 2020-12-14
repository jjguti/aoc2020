with open("input") as f:
    content = [x.strip() for x in f]

def get_addresses(value, mask):
    value = "{:0>36}".format(bin(int(value))[2:])
    mask = [x for x in mask]
    value = [x for x in value]
    exps = []
    for i in range(35, -1, -1):
        if mask[i] in ["1", "X"]:
            value[i] = mask[i] 
    exps.append(value)
    expansions = 1
    while expansions:
        expansions = 0
        for j in range(len(exps)):
            for i in range(0, 36):
                if exps[j][i] == "X":
                    expansions += 1
                    m = exps[j]
                    del(exps[j])
                    m[i] = "0"
                    exps.append(m)
                    m = m.copy()
                    m[i] = "1"
                    exps.append(m)
                    break

    values =  [int("".join(value), base=2) for value in exps]
    return values

mask = 0
mem = {}
for l in content:
    if l.startswith("mask"):
        __, mask = l.split(" = ")
    if l.startswith("mem"):
        pos, value = l.replace("mem[", "").split(" = ")
        pos = int(pos.strip("]").strip(" "))
        for p in get_addresses(pos, mask):
            mem[p] = int(value)

print(sum(mem.values()))
