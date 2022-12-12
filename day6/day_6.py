f = open("input_day_6.txt", "r")

data = f.readline()
i = 0
while i < len(data):
    j = 0
    check = ""
    while j < 4:
        if data[i + j] not in check:
            check += data[i + j]
            j += 1
        else:
            break
    if len(check) == 4:
        print(i + j)
        print(data[i: i+j])
        break
    i += 1

