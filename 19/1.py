with open("input") as f:
    content = [x.strip() for x in f]

def parse_rule(rule):
    name, rule = rule.split(": ")
    rules = rule.split(" | ")
    rules = [x.split(" ") for x in rules]
    return name, rules

def validate_message(rules, rule, message, pos):
    if rule[0][0].startswith("\""):
        return rule[0][0][1] == message[pos], pos + 1
    elif len(rule) == 2:
        rv1, pos1 = validate_message(rules, [rule[0]], message, pos)
        rv2, pos2 = validate_message(rules, [rule[1]], message, pos)
        if rv1:
            return rv1, pos1
        elif rv2:
            return rv2, pos2
        else:
            return False, pos
    else:
        p = pos
        for x in rule[0]:
            rv, new_p = validate_message(rules, rules[x], message, p)
            if not rv:
                return False, pos
            p = new_p
        return True, p

part = 0
rules = {}
messages = []
for c in content:
    if not c:
        part += 1
        continue
    if part == 0: # parsing rules
        name, rule = parse_rule(c)
        rules[name] = rule
    if part == 1: # reading messages
        messages.append(c)

retval = 0
for m in messages:
    rv, pos = validate_message(rules, rules['0'], m, 0)
    if rv and pos == len(m):
        retval += 1

print(retval)
