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
    max_id = 0
    for line in f:
        line = line.strip()
        new_id = calculate_id(*calculate_position(line)) 
        if new_id > max_id:
            max_id = new_id

print(max_id)


