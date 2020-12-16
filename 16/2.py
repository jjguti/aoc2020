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

def validate_ticket(rules, ticket):
    for value in ticket:
        validates = False
        for __, rule in rules.items():
            if validate_rule(rule, value):
                validates = True
                break
        if not validates:
            return False

    return True

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

newtickets = []
newtickets.append(myticket)
for ticket in othertickets:
    if validate_ticket(rules, ticket):
        newtickets.append(ticket)

def validate_row(rule, row):
    return all(map(lambda x: validate_rule(rule,x), row))

final_mapping = {}
new_remaining_rules = rules.copy()
while len(final_mapping) < len(myticket):
    remaining_fields = set(range(0, len(myticket))) - set(final_mapping.values())
    remaining_rules = new_remaining_rules.copy()
    for rulename, rule in remaining_rules.items():
        rows = [(field, [x[field] for x in newtickets]) for field in remaining_fields]
        matching_fields = [fieldno for fieldno, row in rows if validate_row(rule, row)]
        if len(matching_fields) == 1:
            final_mapping[rulename] = matching_fields[0]
            del(new_remaining_rules[rulename])

total = 1
for rulename, fieldno in final_mapping.items():
    if rulename.startswith("departure"):
        total *= myticket[fieldno]

print(total)
