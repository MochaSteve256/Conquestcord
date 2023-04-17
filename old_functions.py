import os
import subprocess


def download_lists():
    if os.path.exists("clans"):
        os.remove("clans")
    else:
        print("The file clans does not exist")
        
    if os.path.exists("players"):
        os.remove("players")
    else:
        print("The file players does not exist")
    runcmd('wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36" https://territorial.io/clans', verbose=True)
    runcmd('wget --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36" https://territorial.io/players', verbose=True)


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
    return "not existing"


def get_info_player(player):
    with open("players", "r", encoding="utf-8") as player_list:
        lines = player_list.readlines() 

    if "data-adblockkey" in lines[0]:
        player_list.close()
        return "error"

    # get rid of \n at end of every element of the list
    global shaped_list1
    shaped_list1 = []
    for line in lines:
        line = line.replace("\n", "")
        line = line.replace(",", "")
        shaped_list1.append(line)

    # check if in any element of the list the desired clan is contained
    for line in shaped_list1:
        if player in line:
            player_list.close()
            return line

    player_list.close()
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
    download_lists()        #downloads the newest version of the clan- and playerlist
    info = get_info_clan(clan)
    if info != "error" and info != "not existing":
        shaped_info = shape_info(info)
        print("Someone checked " + clan)
        return shaped_info
    elif info == "error":
        print("Someone tried to check the clan " + clan + ", but there was an error downloading the list of clans.")
        return "error"
    elif info == "not existing":
        print("Someone tried to check the clan " + clan + ", but this clan does not exist.")
        return "not existing"
    else:
        print("ALERT: There has been an UNKNOWN ERROR while trying to check the clan " + clan)
        return False
    

def get_player_output(player):
    download_lists()        #downloads the newest version of the clan- and playerlist
    info = get_info_player(player)
    if info != "error" and info != "not existing":
        shaped_info = shape_info(info)
        return shaped_info
    elif info == "error":
        print("Someone tried to check the player " + player + ", but there was an error downloading the list of players.")
        return "error"
    elif info == "not existing":
        print("Someone tried to check the player " + player + ", but this player does not exist.")
        return "not existing"
    else:
        print("ALERT: There has been an UNKNOWN ERROR while trying to check the player " + player)
        return False


def get_leaderboard(lenght):
    download_lists()
    with open("clans", "r", encoding="utf-8") as f:
        lines = f.readlines()
    f.close()
    if lenght > 14:
        response = "\n"
        for i in range(lenght):
            line = lines[i]
            response = response + line
        with open("leaderboard.txt", "w", encoding="utf-8") as f:
            f.writelines(response)
            f.close()
            return "leaderboard"
    
    else:
        response = ".\n"
        for i in range(lenght):
            line = lines[i]
            response = response + line
        return response



print("All functions started successfully    (functions.py)")   #always the last line