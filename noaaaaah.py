with open("clans", "r", encoding="utf-8") as f:
    content = f.readlines()
    f.close

shaped_list = []
for line in content:
    line = line.replace("\n", "")
    line = line.replace(",", "")
    shaped_list.append(line)


values = []
for element in shaped_list:
    position = element.find(".")
    position -= 1
    values.append(element[position:])
print(values)

all_points = 0
for value in values:
    try:
        all_points = all_points + float(value)
    except Exception as e:
        print(e)
        pass
print(all_points)