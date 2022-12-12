def calc_res(theirs, mine):
    if theirs == "A":
        if mine == "X":
            return 3
        if mine == "Y":
            return 6
        if mine == "Z":
            return 0
    if theirs == "B":
        if mine == "X":
            return 0
        if mine == "Y":
            return 3
        if mine == "Z":
            return 6
    if theirs == "C":
        if mine == "X":
            return 6
        if mine == "Y":
            return 0
        if mine == "Z":
            return 3

f = open("input_day_2.txt", "r")
result = 0
for line in f:
    theirs = line[0]
    mine = line[2]
    if mine == "X":
        result += 1
    if mine == "Y":
        result += 2
    if mine == "Z":
        result += 3
    result += calc_res(theirs, mine)

print(result)
