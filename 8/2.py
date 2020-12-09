def is_correct(program):
    ip = 0
    acc = 0
    executed = []
    while True:
        if ip in executed:
            return False, 0
        if ip >= len(program):
            return True, acc
        inst, count = program[ip].split(" ")
        executed.append(ip)
        ip += 1
        if inst == "acc":
            acc += int(count)
        if inst == "jmp":
            ip += int(count) - 1

with open("input") as f:
    program = [x.strip() for x in f]

i = 0
for line in program:
    if line.startswith("jmp") or line.startswith("nop"):
        pc = program.copy()
        pc[i] = ("jmp" + line[3:]) if line.startswith("nop") else ("nop" + line[3:])
        correct, acc = is_correct(pc)
        if correct:
            print(acc)
            break
    i += 1
