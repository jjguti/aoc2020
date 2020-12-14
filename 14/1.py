with open("input") as f:
    content = [x.strip() for x in f]

def apply_mask(value, mask):
    value = "{:0>36}".format(bin(int(value))[2:])
    mask = [x for x in mask]
    value = [x for x in value]
    for i in range(35, -1, -1):
        if mask[i] in ["1", "0"]:
            value[i] = mask[i]

    value = int("".join(value), base=2)
    return value

mask = 0
mem = {}
for l in content:
    if l.startswith("mask"):
        __, mask = l.split(" = ")
    if l.startswith("mem"):
        pos, value = l.replace("mem[", "").split(" = ")
        pos = int(pos.strip("]").strip(" "))
        mem[pos] = apply_mask(value, mask)

print(sum(mem.values()))
