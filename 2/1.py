def validate(password, rule, letter):
    count = password.count(letter[0])
    mi, ma = rule.split("-")
    if count >= int(mi) and count <= int(ma):
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
