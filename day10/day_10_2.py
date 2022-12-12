f = open("input_day_10.txt", "r")

cycle = 0
X = 1
grid = [['.' for i in range(40)] for j in range(6)]
for line in f:
    if 'noop' in line:
        if -1 <= (X - (cycle % 40)) <= 1:
            grid[cycle / 40][cycle % 40] = '#'
        cycle += 1
    else :
        info = line.split()
        if -1 <= (X - (cycle % 40)) <= 1:
            grid[cycle/ 40][cycle % 40] = '#'
        cycle += 1
        if -1 <= (X - (cycle % 40)) <= 1:
            grid[cycle/ 40][cycle % 40] = '#'
        cycle += 1
        X += int(info[1])
    print('cycle = ' + str(cycle) + ' (' + str(cycle % 40) + ') & X = ' + str(X))

for row in grid:
        string = ''.join(row)
        print(string)