def count_adjacent(grid, line, seat):
    adj = 0
    if line > 0:
        adj += grid[line-1][max(0, seat-1):seat+2].count("#")
#        print(grid[line-1][max(0, seat-1):seat+2], adj)
    if seat > 0:
        adj += grid[line][seat-1:seat].count("#")
#        print(grid[line][seat-1:seat], adj)
    if seat < len(grid[line]):
        adj += grid[line][seat+1:seat+2].count("#")
#        print(grid[line][seat+1:seat+2], adj)
    if line < len(grid) - 1:
        adj += grid[line+1][max(0, seat-1):seat+2].count("#")
#        print(grid[line+1][max(0, seat-1):seat+2], adj)
    return adj

with open("input") as f:
    content = [[y for y in x.strip()] for x in f]

new = last = content

changes = 1
for line in content:
    print("".join(line))

while changes > 0:
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
            elif status == "#" and adj >= 4:
                new[line][seat] = "L"
                changes += 1
    #    print("".join(adjs))
#    for line in new:
#        print("".join(line))

count = 0
for line in last:
    count += line.count("#")

print(count)
