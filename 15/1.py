content = [2,0,6,12,1,3]

spoken = {}
new_number = 0
last_spoken = 0
turn = 1
for c in content:
    spoken[c] = turn
    last_spoken = c
    turn += 1

was_new = True
for turn in range(len(content) + 1, 2021):
    if was_new:
        new_spoken = 0
    else:
        new_spoken = turn - 1 - last_turn

    was_new = new_spoken not in spoken
    if not was_new:
        last_turn = spoken[new_spoken]
    spoken[new_spoken] = turn
    last_spoken = new_spoken

print(last_spoken)
