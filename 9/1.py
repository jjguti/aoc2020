def find_sum(l, total):
    for i in l:
        m = list(filter(lambda x: i!=x and i + x == total, l))
        if m:
            return True
    return False

with open("input") as f:
    content = [int(x.strip()) for x in f]

r = 25
for i in range(r, len(content)):
    if not find_sum(content[i-r:i], content[i]):
        print(content[i])
        break
