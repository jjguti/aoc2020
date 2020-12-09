def parse_rule(rule_input):
    rule_name, contains = rule_input.replace(" bags", "").replace(" bag", "").split(" contain ")
    rules = {}

    for rule in contains.split(", "):
        rulespl = rule.split(" ", 1)
        if rulespl[0] != "no":
            rules[rulespl[1].strip(".")] = int(rulespl[0])

    return (rule_name, rules)

def find_in_rules(input_rules, color):
    output_rules = {}
    for rule_name, rules in input_rules.items():
        index = 0
        rule_list = list(rules.keys())
        output_rule = rule_list
        while index != len(output_rule):
            if color in output_rule:
                yield rule_name
                break
            for i in range(index, len(output_rule)):
                index += 1
                if rule_list[i] in input_rules.keys():
                    output_rule.extend(input_rules[rule_list[i]])

rules = {}
with open("input") as f:
    for line in f:
        line = line.strip()
        rule_name, rule = parse_rule(line)
        rules[rule_name] = rule

print(len(list(find_in_rules(rules, 'shiny gold'))))
