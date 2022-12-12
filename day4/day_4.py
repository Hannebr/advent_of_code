result = 0
f = open("input_day_4.txt")
for line in f:
    start1 = int(line[:line.find('-')])
    end1 = int(line[line.find('-')+ 1:line.find(',')])
    start2 = int(line[line.find(',')+ 1:line.find('-', 4)])
    end2 = int(line[line.find('-', 4)+ 1:])
    if start1 <= start2 and end1 >= end2:
        result += 1
        print(str(start2) + '-' + str(end2) + ' falls inside ' + str(start1) + '-' + str(end1))
    elif start2 <= start1 and end2 >= end1:
        result += 1
        print(str(start1) + '-' + str(end1) + ' falls inside ' + str(start2) + '-' + str(end2))

print(result)