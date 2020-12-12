with open("input") as f:
    content = [x.strip() for x in f]

east = 90
south = 180
west = 270
north = 0
ns = 0
ew = 0
orientation = east
for ins in content:
    cmd = ins[0]
    number = int(ins[1:])

    if cmd == "N" or (cmd == "F" and orientation == north):
        ns += number
    if cmd == "S" or (cmd == "F" and orientation == south):
        ns -= number
    if cmd == "E" or (cmd == "F" and orientation == east):
        ew += number
    if cmd == "W" or (cmd == "F" and orientation == west):
        ew -= number
    if cmd == "L":
        orientation -= number
    if cmd == "R":
        orientation += number
    while orientation >= 360:
        orientation -= 360
    while orientation < 0:
        orientation += 360

print(abs(ew) + abs(ns))
