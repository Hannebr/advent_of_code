results = []
cals = 0
f = open("input_day_1.txt", "r")
for line in f:
    if line == "\n": 
        results.append(cals)
        cals = 0
    else:
        cals += int(line)
results.sort()
res = results[-1] + results[-2] + results[-3]
print(res)
