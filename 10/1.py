with open("input") as f:
    content = [int(x.strip()) for x in f]

content.sort()
diffs = []
for i in range(len(content) -1 ):
    diffs.append(content[i+1] - content[i])

ones = diffs.count(1) + 1
threes = diffs.count(3) + 1

print(ones * threes)
