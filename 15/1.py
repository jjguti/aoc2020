content = [2,0,6,12,1,3]

spoken = {}
new_spoken = 0
turn = 1
for c in content:
    spoken[c] = turn
    turn += 1

last_turn = 0
while turn <= 2020:
    if not last_turn:
        new_spoken = 0
    else:
        new_spoken = turn - 1 - last_turn

    last_turn = spoken.get(new_spoken, 0)
    spoken[new_spoken] = turn
    turn += 1

print(new_spoken)
