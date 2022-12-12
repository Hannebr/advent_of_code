def check_left(grid):
    for row in grid:
        highest_tree = -1
        for tree in row:
            if tree['height'] > highest_tree:
                tree['visible'] = True
                highest_tree = tree['height']
    return grid

def check_right(grid):
    for row in grid:
        highest_tree = -1
        i = len(row) - 1
        while i >= 0:
            if row[i]['height'] > highest_tree:
                row[i]['visible'] = True
                highest_tree = row[i]['height']
            i -= 1
    return grid

def check_up(grid):
    j = 0
    while (j < len(grid[0])):
        i = 0
        highest_tree = -1
        while (i < len(grid)):
            if grid[i][j]['height'] > highest_tree:
                grid[i][j]['visible'] = True
                highest_tree = grid[i][j]['height']
            i += 1
        j += 1
    return grid

def check_down(grid):
    j = 0
    while (j < len(grid[0])):
        i = len(grid) - 1
        highest_tree = -1
        while (i >= 0):
            if grid[i][j]['height'] > highest_tree:
                grid[i][j]['visible'] = True
                highest_tree = grid[i][j]['height']
            i -= 1
        j += 1
    return grid

def count_visible(grid):
    counter = 0
    for row in grid:
        for tree in row:
            if tree['visible'] == True:
                counter += 1
    return counter

f = open("input_day_8.txt", "r")
grid = []
for line in f:
    row = []
    for tree in line:
        # print(tree)
        if tree == '\n':
            break
        node = {"height": int(tree), "visible": False}
        row.append(node)
    grid.append(row)

grid = check_left(grid)
grid = check_right(grid)
grid = check_up(grid)
grid = check_down(grid)
visible_trees = count_visible(grid)
print(visible_trees)
