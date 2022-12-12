def update_tail(head, tail):
    if head[0] - tail[0] > 1:
        tail[0] += 1
        if head[1] - tail[1] > 0:
            tail[1] += 1
        elif head[1] - tail[1] < 0:
            tail[1] -= 1
    elif head[0] - tail[0] < -1:
        tail[0] -= 1
        if head[1] - tail[1] > 0:
            tail[1] += 1
        elif head[1] - tail[1] < 0:
            tail[1] -= 1
    elif head[1] - tail[1] > 1:
        tail[1] += 1
        if head[0] - tail[0] > 0:
            tail[0] += 1
        elif head[0] - tail[0] < 0:
            tail[0] -= 1
    elif head[1] - tail[1] < -1:
        tail[1] -= 1
        if head[0] - tail[0] > 0:
            tail[0] += 1
        elif head[0] - tail[0] < 0:
            tail[0] -= 1
    return tail

def count_hashes(grid):
    count = 0
    for row in grid:
        for place in row:
            if place == '#':
                count += 1
    return count

f = open("input_day_9.txt", "r")

grid = [['.' for i in range(900)] for j in range(900)]
head = [150, 150]
tail = [150, 150]
grid[tail[0]][tail[1]] = '#'

for line in f:
    info = line.split()
    direction = info[0]
    steps = int(info[1])
    for i in range(steps):
        if direction == 'R':
            head[1] += 1
        elif direction == 'L':
            head[1] -= 1
        elif direction == 'D':
            head[0] += 1
        elif direction == 'U':
            head[0] -= 1
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            tail = update_tail(head, tail)
        grid[tail[0]][tail[1]] = '#'
        print('head = (' + str(head[0]) + ' , ' + str(head[1]) + ')')
        print('tail = (' + str(tail[0]) + ' , ' + str(tail[1]) + ')')


print(count_hashes(grid))