result = 0
f = open("input_day_3.txt", "r")
for line in f:
    comp1 = line[:(len(line)/2)]
    comp2 = line[(len(line)/2):]
    for c in comp1:
        if c in comp2:
            if c.islower():
                result += ord(c) - 96
            elif c.isupper():
                result += ord(c) - 38
            break
print(result)
