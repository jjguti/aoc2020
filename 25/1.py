key1 = 12092626
key2 = 4707356

def get_loop_size(key):
    result = 1
    loop = 1
    while True:
        result *= 7
        result = result % 20201227
        if key == result:
            return loop
        loop += 1

def get_key(subject, loop_size):
    result = 1
    for __ in range(loop_size):
        result *= subject
        result = result % 20201227
    return result

key1_loopsize = get_loop_size(key1)
key2_loopsize = get_loop_size(key2)

print(get_key(key2, key1_loopsize))
print(get_key(key1, key2_loopsize))
