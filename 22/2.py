with open("input") as f:
    content = [x.strip() for x in f]

player1 = []
player2 = []
part = 0
for c in content:
    if not c:
        part += 1
        continue
    if part == 0: # reading player 1 stack
        if c.startswith("Player"):
            continue
        player1.append(int(c))
    if part == 1: # reading player 2 stack
        if c.startswith("Player"):
            continue
        player2.append(int(c))

def play(p1, p2):
    hist1 = list()
    hist2 = list()
    while len(p1) and len(p2):
        if p1 in hist1 and p2 in hist2:
            return 1
        hist1.append(p1.copy())
        hist2.append(p2.copy())

        if p1[0] <= (len(p1) - 1) and p2[0] <= (len(p2) - 1):
            winner = play(p1[1:1+p1[0]], p2[1:1+p2[0]])
        else:
            if p1[0] > p2[0]:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            p1.append(p1[0])
            p1.append(p2[0])
        else:
            p2.append(p2[0])
            p2.append(p1[0])

        del(p1[0])
        del(p2[0])

    if len(p1):
        return 1
    else:
        return 2

w = play(player1, player2)
if w == 1:
    winner = player1
else:
    winner = player2
result = 0

for i in range(len(winner)):
    result += (len(winner) - i ) * winner[i]

print(result)
