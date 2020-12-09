def validate_int(value, mi, ma):
    value = int(value)
    return mi <= value <= ma

def validate_height(value):
    v = int(value[:-2])
    t = value[-2:]
    if (t == "cm" and 150<=v<=193) or (t == "in" and 59<=v<=76):
        return True
    return False

def validate_hex(h):
    return h[0] == "#" and len(h[1:]) == 6 and is_int(h[1:], base=16)

def is_int(x, base=10):
    try:
        int(x, base=base)
    except ValueError:
        return False
    return True

validators = {
    'byr': lambda x: validate_int(x, 1920, 2002),
    'iyr': lambda x: validate_int(x, 2010, 2020),
    'eyr': lambda x: validate_int(x, 2020, 2030),
    'hgt': lambda x: validate_height(x),
    'hcl': lambda x: validate_hex(x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(x) == 9 and is_int(x)
    }


def validate(entry, required_fields):
    for field in required_fields:
        if field not in entry or not validators[field](entry[field]):
            return False

    return True

entries = [{}]
index = 0
with open("input") as f:
    for line in f:
        line = line.strip()
        if not line:
            entries.append({})
            index = index + 1
        else:
            for entry in line.split(" "):
                key, value = entry.split(":")
                entries[index][key] = value

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
print(list(map(lambda x: validate(x, required), entries)).count(True))
