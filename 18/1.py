with open("input") as f:
    content = [x.strip().replace(")", " )").replace("(", "( ").split(" ") for x in f]

def evaluate(expression, startpos):
    result = 0
    operator = "+"
    number = 0
    i = startpos
    while i < len(expression):
        number = None
        if expression[i] == "(":
            number, i = evaluate(expression, i + 1)
        elif expression[i] == ")":
            return result, i
        elif expression[i] in ["*", "+"]:
            operator = expression[i]
        else:
            number = int(expression[i])

        if number is not None:
            if operator == "*":
                result *= number
            elif operator == "+":
                result += number
        i += 1

    return result

print(sum(map(lambda x: evaluate(x, 0), content)))
