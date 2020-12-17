with open("input") as f:
    content = [x.strip() for x in f]

occupied = "#"
free = "."
dimension = 21
initial = int(dimension/3)
x = y = z = initial

grid = [free] * dimension
for z in range(len(grid)):
    grid[z] = [free] * dimension
    for y in range(len(grid[z])):
        grid[z][y] = [free] * dimension

def count_2d_neighbours(grid, z, y, x):
    points = []
    points.append(grid[z][y-1][x-1])
    points.append(grid[z][y-1][x])
    points.append(grid[z][y-1][x+1])
    points.append(grid[z][y][x-1])
    points.append(grid[z][y][x])
    points.append(grid[z][y][x+1])
    points.append(grid[z][y+1][x-1])
    points.append(grid[z][y+1][x])
    points.append(grid[z][y+1][x+1])

    return points.count(occupied)

def count_neighbours(grid, z, y, x):
    count = 0
    count += count_2d_neighbours(grid, z, y, x)
    count += count_2d_neighbours(grid, z-1, y, x)
    count += count_2d_neighbours(grid, z+1, y, x)

    if grid[z][y][x] == occupied:
        count -= 1

    return count


def count_occupied(grid):
    count = 0
    for z in range(len(grid)):
        for y in range(len(grid[z])):
            count += grid[z][y].count(occupied)

    return count

def print_grid(grid):
    for z in range(len(grid)):
        count = 0
        for y in range(len(grid[z])):
            count += grid[z][y].count(occupied)
        if count:
            print(f"z={z}")
            for y in range(len(grid[z])):
                print("".join(grid[z][y]))
            

for x in range(initial, initial + len(content)):
    for y in range(initial, initial + len(content)):
        grid[initial][x][y] = content[x-initial][y-initial]

print_grid(grid)
#print(count_neighbours(grid, initial, initial))

for pass_ in range(6):
    newgrid = [free] * dimension
    for z in range(len(newgrid)):
        newgrid[z] = [free] * dimension
        for y in range(len(newgrid[z])):
            newgrid[z][y] = [free] * dimension

    for z in range(1, len(grid) - 1):
        for y in range(1, len(grid[z]) - 1):
            for x in range(1, len(grid[z][y]) - 1):
                neighbours = count_neighbours(grid, z, y, x)
                if grid[z][y][x] == occupied and neighbours not in [2, 3]:
                    newgrid[z][y][x] = free
                elif grid[z][y][x] == free and neighbours == 3:
                    newgrid[z][y][x] = occupied
                else:
                    newgrid[z][y][x] = grid[z][y][x]

    print(f"pass: {pass_}\n-----------")
    print_grid(newgrid)
    grid = newgrid.copy()

print(count_occupied(grid))
