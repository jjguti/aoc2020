with open("input") as f:
    content = [x.strip().replace(")", " )").replace("(", "( ").split(" ") for x in f]

def evaluate(expression, startpos):
    result = 0
    number = 0
    i = startpos
    expression2 = []
    endpos = startpos
    while i < len(expression):
        number = None
        if expression[i] == "(":
            number, i = evaluate(expression, i + 1)
        elif expression[i] == ")":
            endpos = i
            break
        elif expression[i] == "*":
            expression2.append(result)
            result = 0
        elif expression[i] != "+":
            number = int(expression[i])

        if number is not None:
            result += number
        i += 1

    expression2.append(result)
    result = 1
    for e in expression2:
        result *= e

    return result, endpos

print(sum(map(lambda x: evaluate(x, 0)[0], content)))
