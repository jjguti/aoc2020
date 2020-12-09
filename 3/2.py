def calculate_trees(dx, dy):
    count = 0
    width = None
    x = 0
    y = 0
    with open("input") as f:
        for passline in f:
            if not bool(y % dy):
                passline = passline.strip()
                width = len(passline)
                if passline[x] == "#":
                    count += 1
                x = (x + dx) % width
            y = y + 1
    return(count)

i1 = calculate_trees(1, 1)
i2 = calculate_trees(3, 1)
i3 = calculate_trees(5, 1)
i4 = calculate_trees(7, 1)
i5 = calculate_trees(1, 2)

print(i1*i2*i3*i4*i5)
