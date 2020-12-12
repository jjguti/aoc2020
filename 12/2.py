with open("input") as f:
    content = [x.strip() for x in f]

cos = {90: 0, 180: -1, 270: -0}
sin = {90: 1, 180: 0, 270: -1}
wns = 1
wew = 10
ns = 0
ew = 0

for ins in content:
    rotation = 0
    cmd = ins[0]
    number = int(ins[1:])

    if cmd == "N":
        wns += number
    if cmd == "S":
        wns -= number
    if cmd == "E":
        wew += number
    if cmd == "W":
        wew -= number
    # x' = x * cosx + y * sinx
    # y' = -x * sinx + y * cosx
    if cmd == "L":
        rotation = 360 - number
    if cmd == "R":
        rotation = number
    if cmd == "F":
        ns += (wns*number)
        ew += (wew*number)
    if rotation:
        newew = (wew * cos[rotation]) + (wns * sin[rotation])
        newns = (-wew * sin[rotation]) + (wns * cos[rotation])
        wew = newew
        wns = newns

print(abs(ew) + abs(ns))
