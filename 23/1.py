content = [int(x) for x in "156794823"]
lowest = min(content)
highest = max(content)
original_length = len(content)
for turn in range(100):
    print("--------------------")
    print(f"turn {turn+1}")
    print(content)
    removed = content[1:4]
    print(f"removed : {removed}")
    del(content[1:4])
    content *= 2
    destination = content[0] - 1
    if destination < lowest:
        destination = highest
    while destination in removed:
        destination -= 1
        if destination < lowest:
            destination = highest
    print(f"destination: {destination}")
    destindex = content.index(destination) + 1
    content[destindex:destindex] = removed
    content = content[1:1+original_length]


content *= 2
print(content[content.index(1) + 1: content.index(1) + original_length])
