def check_left(grid, x, y, height):
    z = x - 1
    counter = 0
    highest_tree = -1
    while (z >= 0):
        if grid[y][z] >= highest_tree:
            print(grid[y][z])
            highest_tree = grid[y][z]
        counter += 1
        if grid[y][z] >= height:
            break
        z -= 1
    return counter

def check_right(grid, x, y, height):
    z = x + 1
    counter = 0
    highest_tree = -1
    while (z < len(grid[0])):
        if grid[y][z] >= highest_tree:
            print(grid[y][z])
            highest_tree = grid[y][z]
        counter += 1
        if grid[y][z] >= height:
            break
        z += 1
    return counter

def check_up(grid, x, y, height):
    z = y - 1
    counter = 0
    highest_tree = -1
    while (z >= 0):
        if grid[z][x] >= highest_tree:
            print(grid[z][x])
            highest_tree = grid[z][x]
        counter += 1
        if grid[z][x] >= height:
            break
        z -= 1
    return counter

def check_down(grid, x, y, height):
    z = y + 1
    counter = 0
    highest_tree = -1
    while (z < len(grid)):
        if grid[z][x] >= highest_tree:
            print(grid[z][x])
            highest_tree = grid[z][x]
        counter += 1
        if grid[z][x] >= height:
            break
        z += 1
    return counter

f = open("input_day_8.txt", "r")
grid = []
for line in f:
    row = []
    for tree in line:
        if tree == '\n':
            break
        row.append(int(tree))
    grid.append(row)

highest_score = -1
y = 0
while y < len(grid):
    x = 0
    while x < len(grid[0]):
        left = check_left(grid, x, y, grid[y][x])
        right = check_right(grid, x, y, grid[y][x])
        up = check_up(grid, x, y, grid[y][x])
        down = check_down(grid, x, y, grid[y][x])
        score = (left * right * up * down)
        if score > highest_score:
            highest_score = score
            print('x = ' + str(x) + ' & y = ' + str(y))
        x += 1
    y += 1

# print(grid[82][24])
# print("\n")
# check_left(grid, 24, 82, grid[82][24])
# print("\n")
# check_right(grid, 24, 82, grid[82][24])
# print("\n")
# check_up(grid, 24, 82, grid[82][24])
# print("\n")
# check_down(grid, 24, 82,grid[82][24])
# print("\n")
print(highest_score)