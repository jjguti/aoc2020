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
    ing_ale[al] = poss
    found_ingredients.extend(list(poss))

no_alergens_ing = set(ingredients) - set(found_ingredients)
count = 0
for a in no_alergens_ing:
    for i, al in data:
        count += i.count(a)

print(count)
