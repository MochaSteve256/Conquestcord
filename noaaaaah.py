from itertools import count


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
    count_of_spaces = 0
    temp = ""
    for char in element:
        if char != " ":
            temp = temp.join(char)
        else:
            count_of_spaces += 1
            if count_of_spaces > 1:
                values.append(temp)
                print(values)
            



all_points = 0
for value in values:
    try:
        all_points = all_points + float(value)
        print(value)
    except Exception as e:
        print(e)
        pass
print(int(all_points))