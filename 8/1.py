with open("input") as f:
    program = [x.strip() for x in f]

ip = 0
acc = 0
executed = []
while True:
    if ip in executed:
        break
    inst, count = program[ip].split(" ")
    executed.append(ip)
    ip += 1
    if inst == "acc":
        acc += int(count)
    if inst == "jmp":
        ip += int(count) - 1

print(acc)
