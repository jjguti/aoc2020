with open("input") as f:
    content = [x.strip().strip(")") for x in f]

data = []
for c in content:
    ingredients, alergens = c.split(" (contains ")
    ingredients = ingredients.split(" ")
    alergens = alergens.split(", ")
    data.append((ingredients, alergens))

alergens = []
ingredients = []
for ing, al in data:
    alergens.extend(al)
    ingredients.extend(ing)

alergens = list(set(alergens))
ingredients = list(set(ingredients))
found_ingredients = []
ing_ale = {}
for al in alergens:
    poss = None
    for d in data:
        if al in d[1]:
            if poss is None:
                poss = set(d[0])
            else:
                poss &= set(d[0])
    ing_ale[al] = list(poss)
    found_ingredients.extend(list(poss))

definitives = set()
changes_made = True
while changes_made:
    changes_made = False
    for ale, ing in ing_ale.items():
        if len(ing) == 1 and ing[0] not in definitives:
            definitives.add(ing[0])
            changes_made = True
    for ale, ing in ing_ale.items():
        if len(ing) > 1:
            ingredients = set(ing_ale[ale])
            ing_ale[ale] = list(ingredients - definitives)
            changes_made = True

result = []
for al in sorted(ing_ale.keys()):
    result.append(ing_ale[al][0])

print(",".join(result))
