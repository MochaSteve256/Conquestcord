import functions

functions.download_lists()

with open("clans", "r", encoding="utf-8") as f:
    content = f.readlines()
    

new_content = []
info_about_leaderboard = []
number = "0123456789"
for line in content:
    if not functions.starts_with(line, number):
        info_about_leaderboard.append(line)
    else:
        new_content.append(line)
        
        
shaped_list = []
for line in new_content:
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
        #print("Sucess", value)
    except Exception as e:
        print(e)
        fails.append(value)
        pass
if fails == []:
    print("No Errors Occured")
else:
    print("Errors: ",fails)
print("All Points:" ,all_points)
print("Information from", info_about_leaderboard[0])