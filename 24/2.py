with open("einput") as f:
    content = [x.strip() for x in f]

white = 0
black = 1
floor = [white] * 140
for i in range(len(floor)):
    floor[i] = [white] * 140

prev = None
for m in content:
    x = int(len(floor) / 2)
    y = int(len(floor[0]) / 2)
    for c in m:
        if c == "s":
            y += 1
        elif c == "n":
            y -= 1
        elif c == "e":
            if prev not in ["s"]:
                x += 1
        elif c == "w":
            if prev not in ["n"]:
                x -= 1
        prev = c

    floor[y][x] = white if floor[y][x] == black else black

def count_adjacent(grid, x, y):
    return [
        grid[y][x-1],  # west
        grid[y][x+1],  # east
        grid[y-1][x],  # north-west
        grid[y-1][x+1], # north-east
        grid[y+1][x], # south-east
        grid[y+1][x-1] # south-west
        ].count(black)

for day in range(100):
    new_floor = [white] * len(floor)
    for i in range(len(new_floor)):
        new_floor[i] = floor[i].copy()
    for y in range(1, len(floor) - 1):
        for x in range(1, len(floor[y]) - 1):
            adj = count_adjacent(floor, x, y)
            if floor[y][x] == black and (adj == 0 or adj > 2):
                new_floor[y][x] = white
            elif floor[y][x] == white and adj == 2:
                new_floor[y][x] = black
    floor = new_floor.copy()

result = 0
for x in floor:
    result += x.count(black)

print(result)
