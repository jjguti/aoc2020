entry = set()
total = 0
with open("input") as f:
    for line in f:
        line = line.strip()
        if not line:
            total += len(entry)
            entry = set()
        else:
            entry = set(line) | set(entry)
    total += len(entry)

print(total)
