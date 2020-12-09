with open("input") as f:
    content = [int(x.strip()) for x in f]

target = 22406676
for i in range(len(content)):
    for length in range(2, len(content) - i):
        subset = content[i:i+length]
        s = sum(subset)
        if s == target:
            print(min(subset) + max(subset))
        if s > target:
            break
