entry = set()
total = 0
new_group = True
with open("input") as f:
    for line in f:
        line = line.strip()
        if not line:
            total += len(entry)
            entry = set()
            new_group = True
        else:
            if new_group:
                new_group = False
                entry = set(line)
            else:
                entry = set(line) & entry
    total += len(entry)

print(total)
