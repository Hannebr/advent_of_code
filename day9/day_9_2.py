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
t1 = [150, 150]
t2 = [150, 150]
t3 = [150, 150]
t4 = [150, 150]
t5 = [150, 150]
t6 = [150, 150]
t7 = [150, 150]
t8 = [150, 150]
t9 = [150, 150]
grid[t9[0]][t9[1]] = '#'

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
        if abs(head[0] - t1[0]) > 1 or abs(head[1] - t1[1]) > 1:
            t1 = update_tail(head, t1)
        if abs(t1[0] - t2[0]) > 1 or abs(t1[1] - t2[1]) > 1:
            t2 = update_tail(t1, t2)
        if abs(t2[0] - t3[0]) > 1 or abs(t2[1] - t3[1]) > 1:
            t3 = update_tail(t2, t3)
        if abs(t3[0] - t4[0]) > 1 or abs(t3[1] - t4[1]) > 1:
            t4 = update_tail(t3, t4)
        if abs(t4[0] - t5[0]) > 1 or abs(t4[1] - t5[1]) > 1:
            t5 = update_tail(t4, t5)
        if abs(t5[0] - t6[0]) > 1 or abs(t5[1] - t6[1]) > 1:
            t6 = update_tail(t5, t6)
        if abs(t6[0] - t7[0]) > 1 or abs(t6[1] - t7[1]) > 1:
            t7 = update_tail(t6, t7)
        if abs(t7[0] - t8[0]) > 1 or abs(t7[1] - t8[1]) > 1:
            t8 = update_tail(t7, t8)
        if abs(t8[0] - t9[0]) > 1 or abs(t8[1] - t9[1]) > 1:
            t9 = update_tail(t8, t9)
        grid[t9[0]][t9[1]] = '#'
        print('head = (' + str(head[0]) + ' , ' + str(head[1]) + ')')
        print('tail = (' + str(t9[0]) + ' , ' + str(t9[1]) + ')')


print(count_hashes(grid))