f = open("input_day_7.txt", "r")
results = {}
dir_links = {}
data = f.readlines()
t = {"name": '/', "size": 0, "children": []}
i = 0
while i < len(data):
    if "$ ls" in data[i]:
        j = 1
        print(data[i])
        size = 0
        list_dirs = []
        while (i + j) < len(data):
            if "$" in data[i + j]:
                break
            if "dir" not in data[i + j]:
                data_spl = data[i + j].split()
                print(data_spl)
                size += int(data_spl[0])
            else:
                data_spl = data[i + j].split()
                node = {"name" = data_spl[1], size}
                list_dirs.append(data_spl[1])
            j += 1
        if size < 100000:
            name = data[i - 1].split()
            results.update({name[2]: size})
            dir_links.update({name[2]: list_dirs})
        i += j 
    else:
        i += 1
# print(results)
print("\nBefore:\n")
print(dir_links)
sorted_links = sorted(dir_links, key=lambda k: len(dir_links[k]))
print("\nAfter:\n")
print(sorted_links)