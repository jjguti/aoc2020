with open("input") as f:
    content = [x.strip() for x in f]

occupied = "#"
free = "."
dimension = 21
initial = int(dimension/3)
x = y = z = w = initial

def count_4d_neighbours(grid, w, z, y, x):
    count = 0
    for w_ in range(w-1, w +2):
        for z_ in range(z-1, z+2):
            for y_ in range(y-1, y+2):
                for x_ in range(x-1, x+2):
                    if grid[w_][z_][y_][x_] == occupied:
                        count +=1

    if grid[w][z][y][x] == occupied:
        count -= 1

    return count


def count_occupied(grid):
    count = 0
    for w in range(len(grid)):
        for z in range(len(grid[w])):
            for y in range(len(grid[w][z])):
                count += grid[w][z][y].count(occupied)

    return count

def print_grid(grid):
    for w in range(len(grid)):
        for z in range(len(grid[w])):
            count = 0
            for y in range(len(grid[w][z])):
                count += grid[w][z][y].count(occupied)
            if count:
                print(f"w={w} z={z}")
                for y in range(len(grid[w][z])):
                    print("".join(grid[w][z][y]))
                
grid = [None] * dimension
for w in range(len(grid)):
    grid[w] = [None] * dimension
    for z in range(len(grid[w])):
        grid[w][z] = [None] * dimension
        for y in range(len(grid[w][z])):
            grid[w][z][y] = [free] * dimension

for x in range(initial, initial + len(content)):
    for y in range(initial, initial + len(content)):
        grid[initial][initial][x][y] = content[x-initial][y-initial]

print_grid(grid)
#print(count_neighbours(grid, initial, initial))

for pass_ in range(6):
    newgrid = [free] * dimension
    for w in range(len(newgrid)):
        newgrid[w] = [free] * dimension
        for z in range(len(newgrid[w])):
            newgrid[w][z] = [free] * dimension
            for y in range(len(newgrid[w][z])):
                newgrid[w][z][y] = [free] * dimension

    for w in range(1, len(grid) - 1):
        for z in range(1, len(grid[w]) - 1):
            for y in range(1, len(grid[w][z]) - 1):
                for x in range(1, len(grid[w][z][y]) - 1):
                    neighbours = count_4d_neighbours(grid, w, z, y, x)
                    if grid[w][z][y][x] == occupied and neighbours not in [2, 3]:
                        newgrid[w][z][y][x] = free
                    elif grid[w][z][y][x] == free and neighbours == 3:
                        newgrid[w][z][y][x] = occupied
                    else:
                        newgrid[w][z][y][x] = grid[w][z][y][x]

    print(f"pass: {pass_}\n-----------")
    print_grid(newgrid)
    grid = newgrid.copy()

print(count_occupied(grid))
