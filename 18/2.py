with open("input") as f:
    content = [x.strip().replace(")", " )").replace("(", "( ").split(" ") for x in f]

def evaluate(expression, startpos):
    sumresult = 0
    number = 0
    i = startpos
    endpos = None
    mulresult = 1
    while i < len(expression):
        number = None
        if expression[i] == "(":
            number, i = evaluate(expression, i + 1)
        elif expression[i] == ")":
            endpos = i
            break
        elif expression[i] == "*":
            mulresult *= sumresult
            sumresult = 0
        elif expression[i] != "+":
            number = int(expression[i])

        if number is not None:
            sumresult += number
        i += 1

    mulresult *= sumresult

    return mulresult, endpos

print(sum(map(lambda x: evaluate(x, 0)[0], content)))
