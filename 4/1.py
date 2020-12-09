def validate(entry, required_fields):
    for field in required_fields:
        if field not in entry:
            return False

    return True

entries = []
entry = {}
with open("input") as f:
    for line in f:
        line = line.strip()
        if not line:
            entries.append(entry)
            entry = {}
        else:
            for field in line.split(" "):
                key, value = field.split(":")
                entry[key] = value
    entries.append(entry)

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
print(list(map(lambda x: validate(x, required), entries)).count(True))
