def first_of(haystack, needles):
    element = len(haystack) - 1
    for needle in needles:
        if needle in haystack:
            element = min(haystack.index(needle), element)
    return haystack[element] if haystack else ""

def count_adjacent(grid, line, seat):
    adjs = []
    h = len(grid) - 1
    w = len(grid[0]) - 1
    # generate lists
    #
    #   D1  V1  D2
    #   H1  XX  H2
    #   D3  V2  D4
    #
    # vertical lists
    v1 = []
    if line > 0:
        for x in range(line - 1, -1, -1):
            v1.append(grid[x][seat])

    v2 = []
    if line < w:
        for x in range(line + 1, len(grid)):
            v2.append(grid[x][seat])

    # horizontal lists
    h1 = []
    if seat > 0:
        h1 = grid[line][seat - 1::-1]
    h2 = grid[line][seat+1:]

    # diagonal lists
    d1 = []
    s = seat - 1
    l = line - 1
    for __ in range(min(line, seat)):
        d1.append(grid[l][s])
        l -=1
        s -=1

    d2 = []
    s = seat + 1
    l = line - 1
    for __ in range(min(line, w - seat)):
        d2.append(grid[l][s])
        l -=1
        s +=1

    d3 = []
    s = seat - 1
    l = line + 1
    for __ in range(min(h - line, seat)):
        d3.append(grid[l][s])
        l +=1
        s -=1

    d4 = []
    s = seat + 1
    l = line + 1
    for __ in range(min(h - line, w - seat)):
        d4.append(grid[l][s])
        l +=1
        s +=1

    adjs.append(first_of(v1, ["#", "L"]))
    adjs.append(first_of(v2, ["#", "L"]))
    adjs.append(first_of(h1, ["#", "L"]))
    adjs.append(first_of(h2, ["#", "L"]))
    adjs.append(first_of(d1, ["#", "L"]))
    adjs.append(first_of(d2, ["#", "L"]))
    adjs.append(first_of(d3, ["#", "L"]))
    adjs.append(first_of(d4, ["#", "L"]))

    return adjs.count("#")

with open("input") as f:
    content = [[y for y in x.strip()] for x in f]

new = last = content

changes = 1
#for line in content:
#    print("".join(line))

iterations = 0
while changes > 0:
    iterations += 1
#    print(".", end="", flush=True)
    last = []
    for line in new:
        last.append(line.copy())
    changes = 0
    for line in range(len(last)):
        adjs = []
        for seat in range(len(last[line])):
            status = last[line][seat]
            adj = count_adjacent(last, line, seat)
            adjs.append(str(adj))
            if status == "L" and adj == 0:
                new[line][seat] = "#"
                changes += 1
            elif status == "#" and adj >= 5:
                new[line][seat] = "L"
                changes += 1
#        print("".join(adjs), "".join(new[line]))
#    for line in new:
#        print("".join(line))

#for line in new:
#    print("".join(line))


count = 0
for line in last:
    count += line.count("#")

print(count)
