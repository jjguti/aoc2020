def calculate_position(code):
    rowt = 128
    rowb = 0
    colb = 0
    colt = 8
    for l in code[:7]:
        if l == "F":
            rowt = (rowt + rowb) / 2
        else:
            rowb = (rowt + rowb) / 2

    for l in code[7:]:
        if l == "L":
            colt = (colt + colb) / 2
        else:
            colb = (colt + colb) / 2

    return int(rowt-1), int(colt-1)

def calculate_id(row, col):
    return (row * 8) + col

with open("input") as f:
    ids = []
    for line in f:
        line = line.strip()
        new_id = calculate_id(*calculate_position(line)) 
        ids.append(new_id)

ids.sort()
for i in range(len(ids) - 1):
    if ids[i] + 2 == ids[i+1]:
        print(ids[i] + 1)
