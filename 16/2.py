from collections import OrderedDict

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
rules = OrderedDict()
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

possible_mappings = OrderedDict()
for field in range(0, len(myticket)):
    for rulename, rule in rules.items():
        validates = True
        for ticket in newtickets:
            if not validate_rule(rule, ticket[field]):
                validates = False
        if validates:
            if rulename not in possible_mappings:
                possible_mappings[rulename] = []
            possible_mappings[rulename].append(field)

mappings_lengths = [len(x) for __, x in possible_mappings.items()]
mappings_names = list(possible_mappings.keys())

final_mapping = OrderedDict()
already_assigned = []
for length in sorted(mappings_lengths):
    mapping_index = mappings_lengths.index(length)
    rule_name = mappings_names[mapping_index]
    pos_maps = possible_mappings[rule_name]
    definitive_maps = list(filter(lambda x: x not in already_assigned, pos_maps))
    already_assigned.extend(definitive_maps)
    final_mapping[rule_name] = definitive_maps[0]
    
total = 1
for rulename, fieldno in final_mapping.items():
    if rulename.startswith("departure"):
        total *= myticket[fieldno]

print(total)
