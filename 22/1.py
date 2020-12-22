with open("input") as f:
    content = [x.strip() for x in f]

player1 = []
player2 = []
part = 0
for c in content:
    if not c:
        part += 1
        continue
    if part == 0: # reading player 2 stack
        if c.startswith("Player"):
            continue
        player1.append(int(c))
    if part == 1: # reading player 1 stack
        if c.startswith("Player"):
            continue
        player2.append(int(c))

while len(player1) and len(player2):
    if player1[0] > player2[0]:
        player1.append(player1[0])
        player1.append(player2[0])
        del(player1[0])
        del(player2[0])
    else:
        player2.append(player2[0])
        player2.append(player1[0])
        del(player1[0])
        del(player2[0])

if len(player1):
    winner = player1
else:
    winner = player2

result = 0
for i in range(len(winner)):
    result += (len(winner) - i ) * winner[i]

print(result)
