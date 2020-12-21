with open("input") as f:
    content = [x.strip() for x in f]

def simplify_tile(tile):
    result = []
    result.append(tile[0])
    result.append("".join([x[0] for x in tile]))
    result.append("".join([x[-1] for x in tile]))
    result.append(tile[-1])
    return result

tiles = {}
new_tile = []
for c in content:
    if not c:
        tiles[tile_id] = simplify_tile(new_tile)
        new_tile = []
    elif c.startswith("Tile"):
        tile_id = int(c[5:-1])
    else:
        new_tile.append(c)

def find_match(tiles, tile_id, border):
    for t_id, tile in tiles.items():
        if t_id != tile_id:
            for b in tile:
                if b == border or b == "".join(list(reversed(border))):
                    return True

    return False

result = 1
for tile_id, tile in tiles.items():
    if list(map(lambda x: find_match(tiles, tile_id, x), tile)).count(True) == 2:
        result *= tile_id

print(result)
