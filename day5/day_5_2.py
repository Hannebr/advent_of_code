def print_grid(grid):
    for key in grid:
        print(grid[key])

grid = {1: ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V'],
    2: ['S', 'R', 'L', 'M', 'J', 'D', 'Q'],
    3: ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B'],
    4: ['R', 'S', 'C', 'L'],
    5: ['M', 'V', 'T', 'P', 'F', 'B'],
    6: ['T', 'R', 'Q', 'N', 'C'],
    7: ['G', 'V', 'R'],
    8: ['C', 'Z', 'S', 'P', 'D', 'L', 'R'],
    9: ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']}

grid1 = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}

f = open("input_day_5.txt", "r")
for line in f:
    data = line.split()
    num = int(data[1])
    src = int(data[3])
    dst = int(data[5])
    tmp = grid[src][(num * -1):]
    grid[src] = grid[src][:(num * -1)]
    for crate in tmp:
        grid[dst].append(crate)
print_grid(grid)
for key in grid:
    print(grid[key][-1])