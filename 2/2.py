def validate(password, rule, letter):
    p1, p2 = rule.split("-")
    p1 = int(p1) - 1
    p2 = int(p2) - 1
    if (password[p1] == letter[0]) != (password[p2] == letter[0]):
        return True
    else:
        return False

count = 0
with open("input") as f:
    for passline in f:
        rule, letter, password = passline.split(" ")
        if validate(password, rule, letter):
            count = count + 1

print(count)
