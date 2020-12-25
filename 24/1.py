with open("input") as f:
    content = [x.strip() for x in f]

white = 0
black = 1
floor = [white] * 50
for i in range(len(floor)):
    floor[i] = [white] * 50

prev = None
for m in content:
    x = 25
    y = 25
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
        if c in ["e", "w"]:
            if prev in ["n", "s"]:
                print(f"{prev}{c}", x,y)
            else:
                print(c, x,y)
        prev = c

    print(f"switching {x},{y} from {floor[y][x]}")
    floor[y][x] = white if floor[y][x] == black else black

result = 0
for x in floor:
    result += x.count(black)

print(result)
