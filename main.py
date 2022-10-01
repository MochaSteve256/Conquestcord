import os
import subprocess

if os.path.exists("clans"):
    os.remove("clans")
else:
    print("The file does not exist")


if os.path.exists("players"):
    os.remove("players")
else:
    print("The file does not exist")


def runcmd(cmd, verbose=False, *args, **kwargs):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass


def get_info_clan(clan):
    with open("clans", "r", encoding="utf-8") as f:
        lines = f.readlines() 

    if "data-adblockkey" in lines[0]:
        f.close()
        print("There was an error downloading the list of clans, please try again later.")
        return "error"

    # get rid of \n at end of every element of the list
    global shaped_list
    shaped_list = []
    for line in lines:
        line = line.replace("\n", "")
        line = line.replace(",", "")
        shaped_list.append(line)

    # check if in any element of the list the desired clan is contained
    for line in shaped_list:
        if clan.upper() in line:
            f.close()
            return line

    f.close()
    print("Some user requested a player that doesn't exist. Infromation from " + shaped_list[0])
    return "not existing"


def get_info_player(player):
    with open("players", "r", encoding="utf-8") as f1:
        lines2 = f1.readlines() 

    if "data-adblockkey" in lines2[0]:
        f1.close()
        print("There was an error downloading the list of players.")
        return "error"

    # get rid of \n at end of every element of the list
    global shaped_list1
    shaped_list1 = []
    for line in lines2:
        line = line.replace("\n", "")
        line = line.replace(",", "")
        shaped_list1.append(line)

    # check if in any element of the list the desired clan is contained
    for line in shaped_list1:
        if player.upper() in line:
            f1.close()
            return line

    f1.close()
    print("There doesn't exist a player with this name yet! Information from " + shaped_list1[0])
    return "not existing"


def shape_info(info):
    info = list(info)
    info.append(" ")
    output = []
    temp = ""
    for element in info:
        if element != " ":  # checks if character is a number or a space
            temp = temp + element  # speichert zusammenhängende Buchstaben in einer temporären Variable
        else:
            output.append(temp)  # appends temporary variable to output as soon as space is registered
            temp = ""
    return output


def get_clan_output(clan):
    info = get_info_clan(clan)
    if info != "error" and info != "not existing":
        shaped_info = shape_info(info)
        print("Someone checked " + clan)
        return shaped_info
    elif info == "error":
        print("Someone tried to check " + clan + ", but there was an error downloading the list of clans.")
        return "error"
    elif info == "not existing":
        return "not existing"
    else:
        return False
    

def get_player_output(player):
    info = get_info_player(player)
    if info != "error" and info != "not existing":
        shaped_info = shape_info(info)
        return shaped_info
    elif info == "error":
        return "error"
    elif info == "not existing":
        return "not existing"
    else:
        return False


runcmd('wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36" https://territorial.io/clans', verbose=True)


runcmd('wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36" https://territorial.io/players', verbose=True)



print("main.py started successfully")   #always the last line