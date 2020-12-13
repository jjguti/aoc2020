def is_correct_timestamp(buses, timestamp):
    for pos, bus in buses:
        if (timestamp + pos) % bus != 0:
                return False
    return True

# t -> initial timestamp
# dx -> dx
def doa2(buses, t, dx):
    timestamp = t
    while True:
        if is_correct_timestamp(buses, timestamp):
            break
        timestamp += dx

    return timestamp

with open("input") as f:
    content = [x.strip() for x in f]

splcont = content[1].split(",")
tbuses = zip(range(len(splcont)), [int(x) if x != "x" else None for x in splcont])
buses = list(filter(lambda x: x[1] != None, tbuses))

dx = buses[0][1]
t = buses[0][0]
for i in range(1, len(buses)):
    t = doa2(buses[i:i+2], t, dx)
    dx *= buses[i][1]

print(t)
