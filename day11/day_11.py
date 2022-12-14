from re import sub

class Monkey:
    def __init__(self, items, operation, test, true_dir, false_dir):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_dir = true_dir
        self.false_dir = false_dir
        self.inspects = 0
    
    def run_operation(self, item):
        if self.operation[2] == 'old':
            worry = item * item
        elif self.operation[1] == '*':
            worry = item * int(self.operation[2])
        elif self.operation[1] == '+':
            worry = item + int(self.operation[2])
        worry /= 3
        return worry

    def run_test(self, item):
        if item % self.test == 0:
            return True
        return False

f = open("input_day_11.txt", "r")
monkeys = []
lines = f.readlines()
i = 0
while i < len(lines):
    j = 0
    while True:
        if i + j >= len(lines):
            break
        elif lines[i+j] == '\n':
            j += 1
            break
        # print(lines[i + j])
        if 'Starting items' in lines[i + j]:
            items_s = lines[i + j].split()
            items_s = items_s[2:]
            items = []
            for item in items_s:
                item = sub(',', '', item)
                items.append(int(item))
            # print(items)
        elif 'Operation' in lines[i + j]:
            operation_s = lines[i + j].split()
            operation = operation_s[3:]
            # print(operation)
        elif 'Test' in lines[i + j]:
            test_s = lines[i + j].split()
            test = int(test_s[-1])
            # print(test)
        elif 'true' in lines[i + j]:
            true_s = lines[i + j].split()
            true_dir = int(true_s[-1])
            # print(true_dir)
        elif 'false' in lines[i + j]:
            false_s = lines[i + j].split()
            false_dir = int(false_s[-1])
            # print(false_dir)
        j += 1
    i += j
    monk = Monkey(items, operation, test, true_dir, false_dir)
    monkeys.append(monk)

for k in range(20):
    for i in range(len(monkeys)):
        # print('Monkey' + str(i))
        # print(monkeys[i].items)
        # print(len(monkeys[i].items))
        j = 0
        while len(monkeys[i].items) > 0:
            worry_level = monkeys[i].run_operation(monkeys[i].items[0])
            monkeys[i].inspects += 1
            # print('Old worry level = ' + str(monkeys[i].items[0]) + ', New worry level = ' + str(worry_level))
            monkeys[i].items.pop(0)
            if monkeys[i].run_test(worry_level):
                monkeys[monkeys[i].true_dir].items.append(worry_level)
                # print('thrown to monkey ' + str(monkeys[i].true_dir))
            else:
                monkeys[monkeys[i].false_dir].items.append(worry_level)
                # print('thrown to monkey ' + str(monkeys[i].false_dir))
            # print(monkeys[i].items)

insp_list = [] 
for i in range(len(monkeys)):
    insp_list.append(monkeys[i].inspects)

insp_list.sort()
print(421 *433)