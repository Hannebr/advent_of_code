def calc_mine(theirs, res):
    if theirs == "A":
        if res == "X":
            return 3
        if res == "Y":
            return 1
        if res == "Z":
            return 2
    if theirs == "B":
        if res == "X":
            return 1
        if res == "Y":
            return 2
        if res == "Z":
            return 3
    if theirs == "C":
        if res == "X":
            return 2
        if res == "Y":
            return 3
        if res == "Z":
            return 1

f = open("input_day_2.txt", "r")
result = 0
for line in f:
    theirs = line[0]
    res = line[2]
    if res == "X":
        result += 0
    if res == "Y":
        result += 3
    if res == "Z":
        result += 6
    result += calc_mine(theirs, res)

print(result)
