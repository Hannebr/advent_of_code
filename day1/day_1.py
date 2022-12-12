results = []
cals = 0
f = open("input_day_1.txt", "r")
for line in f:
    if line == "\n": 
        results.append(cals)
        cals = 0
    else:
        cals += int(line)
res = max(results)
print(res)
