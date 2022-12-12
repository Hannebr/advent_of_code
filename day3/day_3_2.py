# stop cheating and hardcODE :P
result = 0
f = open("input_day_3.txt", "r")
while (True):
    elf1 = f.readline()
    if not elf1:
        break
    elf2 = f.readline()
    if not elf2:
        break
    elf3 = f.readline()
    if not elf3:
        break
    for c in elf1:
        if c in elf2:
            if c in elf3:
                if c.islower():
                    result += ord(c) - 96
                elif c.isupper():
                    result += ord(c) - 38
                break
print(result)