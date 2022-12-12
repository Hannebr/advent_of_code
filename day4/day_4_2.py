result = 0
f = open("input_day_4.txt")
for line in f:
    start1 = int(line[:line.find('-')])
    end1 = int(line[line.find('-')+ 1:line.find(',')])
    start2 = int(line[line.find(',')+ 1:line.find('-', 4)])
    end2 = int(line[line.find('-', 4)+ 1:])
    if end1 < start2 or end2 < start1:
        print(str(start2) + '-' + str(end2) + ' dont overlap ' + str(start1) + '-' + str(end1))
    else:
        result += 1
print(result)