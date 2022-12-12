f = open("input_day_10.txt", "r")

cycle = 0
X = 1
sum = 0
for line in f:
    if 'noop' in line:
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            print('signal strength : ' + str(cycle) + ' * ' + str(X) + ' = ' + str(cycle * X))
            sum += cycle * X
    else :
        info = line.split()
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            print('signal strength : ' + str(cycle) + ' * ' + str(X) + ' = ' + str(cycle * X))
            sum += cycle * X
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            print('signal strength : ' + str(cycle) + ' * ' + str(X) + ' = ' + str(cycle * X))
            sum += cycle * X
        X += int(info[1])
print(sum)