def play_number_of_turns(turns):
    content = [2,0,6,12,1,3]

    spoken = [0] * turns
    new_spoken = 0
    turn = 1
    for c in content:
        spoken[c] = turn
        turn += 1

    last_turn = 0
    while turn <= turns:
        if not last_turn:
            new_spoken = 0
        else:
            new_spoken = turn - 1 - last_turn

        last_turn = spoken[new_spoken]
        spoken[new_spoken] = turn
        turn += 1

    print(new_spoken)

play_number_of_turns(30000000)
