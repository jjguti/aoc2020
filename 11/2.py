def count_adjacent(grid, line, seat):
    h = len(grid) - 1
    w = len(grid[0]) - 1
    # generate lists
    #
    #   D1  V1  D2
    #   H1  XX  H2
    #   D3  V2  D4
    #
    # vertical lists
    adj = 0
    if line > 0:
        for x in range(line - 1, -1, -1):
            if grid[x][seat] == "#":
                adj += 1
                break
            if grid[x][seat] == "L":
                break

    if line < w:
        for x in range(line + 1, len(grid)):
            if grid[x][seat] == "#":
                adj += 1
                break
            if grid[x][seat] == "L":
                break

    # horizontal lists
    if seat > 0:
        for s in range(seat - 1, -1, -1):
            if grid[line][s] == "#":
                adj += 1
                break
            if grid[line][s] == "L":
                break
    for s in range(seat + 1, w+1):
        if grid[line][s] == "#":
            adj += 1
            break
        if grid[line][s] == "L":
            break


    # diagonal lists
    s = seat - 1
    l = line - 1
    for __ in range(min(line, seat)):
        if grid[l][s] == "#":
            adj += 1
            break
        if grid[l][s] == "L":
            break
        l -=1
        s -=1

    s = seat + 1
    l = line - 1
    for __ in range(min(line, w - seat)):
        if grid[l][s] == "#":
            adj += 1
            break
        if grid[l][s] == "L":
            break
        l -=1
        s +=1

    s = seat - 1
    l = line + 1
    for __ in range(min(h - line, seat)):
        if grid[l][s] == "#":
            adj += 1
            break
        if grid[l][s] == "L":
            break
        l +=1
        s -=1

    s = seat + 1
    l = line + 1
    for __ in range(min(h - line, w - seat)):
        if grid[l][s] == "#":
            adj += 1
            break
        if grid[l][s] == "L":
            break
        l +=1
        s +=1

    return adj

with open("input") as f:
    content = [[y for y in x.strip()] for x in f]

new = last = content

changes = 1
#for line in content:
#    print("".join(line))

iterations = 0
while changes > 0:
    iterations += 1
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

#for line in new:
#    print("".join(line))


count = 0
for line in last:
    count += line.count("#")

print(count)
