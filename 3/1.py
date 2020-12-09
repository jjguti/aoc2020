count = 0
width = None
x = 0
with open("input") as f:
    for passline in f:
        passline = passline.strip()
        width = len(passline)
        if passline[x] == "#":
            count += 1
        x = (x + 3) % width

print(count)
