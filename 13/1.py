with open("input") as f:
    content = [x.strip() for x in f]

timestamp = int(content[0])
buses = [int(x) for x in content[1].split(",") if x != "x"]
next_deps = [((int(timestamp / x) + 1) * x) - timestamp for x in buses]
next_dep = min(next_deps)
next_bus = buses[next_deps.index(next_dep)]
print(next_bus * next_dep)
