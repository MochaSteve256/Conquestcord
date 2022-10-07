with open("clans", "r", encoding="utf-8") as f:
    content = f.readlines()
    f.close()

shaped_list = []
for line in content:
    line = line.replace("\n", "")
    line = line + ","
    shaped_list.append(line)


values = []
for element in shaped_list:
    count_of_commata = 0
    temp = ""
    for char in element:
        if char != ",":
            temp = temp + char
        else:
            if count_of_commata > 1:
                values.append(temp)
                temp = ""
            else:
                temp = ""
                count_of_commata += 1

all_points = 0
fails = []
for value in values:
    try:
        all_points = all_points + float(value)
        print("Sucess", value)
    except Exception as e:
        print(e)
        fails.append(value)
        pass
print(fails)
print(all_points)
