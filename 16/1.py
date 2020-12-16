with open("input") as f:
    content = [x.strip() for x in f]

def parse_rule(rule):
    name, rest = rule.split(": ")
    rule1, rule2 = rest.split(" or ")
    rules = []
    for i in rule1, rule2:
        mi, ma = i.split("-")
        rules.append((int(mi), int(ma)))

    return name, rules

def validate_rule(rule, value):
    validates = False
    for r in rule:
        mi, ma = r
        if value >= mi and value <= ma:
            validates = True
    return validates

part = 0
rules = {}
othertickets = []
myticket = []
for c in content:
    if not c:
        part += 1
        continue
    if part == 0: # parsing rules
        name, rule = parse_rule(c)
        rules[name] = rule
    if part == 1: # parsing your ticket
        if c.startswith("your ticket"):
            continue
        myticket = [int(x) for x in c.split(",")]
    if part == 2: # parsing other tickets
        if c.startswith("nearby tickets"):
            continue
        othertickets.append([int(x) for x in c.split(",")])

total = 0
for ticket in othertickets:
    for value in ticket:
        validates = False
        for __, rule in rules.items():
            if validate_rule(rule, value):
                validates = True
                break
        if not validates:
            total += value

print(total)
