with open("input") as f:
    content = [x.strip() for x in f]

def parse_rule(rule):
    name, rule = rule.split(": ")
    rules = rule.split(" | ")
    rules = [x.split(" ") for x in rules]
    return name, rules

def expand_rule(rules, rulename):
    rule = rules[rulename]
    for i in range(len(rule)):
        for x in range(len(rule[i])):
            if rule[i][x].startswith("\""):
                yield rule[i][x]
            else:
                yield list(expand_rule(rules, rules[rulename][i][x]))

def max_length(rules, rule):
    if rule[0][0].startswith("\""):
        return 1
    elif len(rule) == 2:
        return max_length(rules, [rule[0]])
    else:
        retval = 0
        for x in rule[0]:
            retval += max_length(rules, rules[x])
        return retval

def validate_message(rules, rule, message):
    if max_length(rules, rule) != len(message):
        return False
    if rule[0][0].startswith("\""):
        return rule[0][0][1] == message
    elif len(rule) == 2:
        l = max_length(rules, [rule[0]])
        return (validate_message(rules, [rule[0]], message[:l]) or
                validate_message(rules, [rule[1]], message[:l]))
    else:
        retval = True
        pos = 0
        for x in rule[0]:
            l = max_length(rules, rules[x])
            retval &= validate_message(rules, rules[x], message[pos:pos+l])
            pos += l
        return retval

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
    if validate_message(rules, rules['0'], m):
        retval += 1

print(retval)
