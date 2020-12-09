def parse_rule(rule_input):
    rule_name, contains = rule_input.replace(" bags", "").replace(" bag", "").split(" contain ")
    rules = {}

    for rule in contains.split(", "):
        rulespl = rule.split(" ", 1)
        if rulespl[0] != "no":
            rules[rulespl[1].strip(".")] = int(rulespl[0])

    return (rule_name, rules)

def count_bags(input_rules, color):
    total = 1
    for rule, count in input_rules[color].items():
        total += (count * count_bags(input_rules, rule))

    return total

rules = {}
with open("input") as f:
    for line in f:
        line = line.strip()
        rule_name, rule = parse_rule(line)
        rules[rule_name] = rule

print(count_bags(rules, 'shiny gold') - 1)
