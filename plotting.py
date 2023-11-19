import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from time import sleep as sl
import time
import json
import threading
import numpy as np

import functions

timestamps = []
x = []
points = []
rank = []

def sleep_until_next_hour():
    # Get the current time in seconds since the epoch
    current_time = time.time()

    # Calculate the number of seconds until the next full hour
    seconds_until_next_hour = 3600 - (current_time % 3600)

    # Sleep until the next full hour is reached
    time.sleep(seconds_until_next_hour)

def plot(clan):
    
    fig, ax1 = plt.subplots(figsize=(10, 5))
    plt.title(clan)

    ax1.set_xlabel('Date/Time')
    ax1.set_ylabel('Points', color='red')
    ax1.plot(x, points, color='red', marker='o')
    ax1.tick_params(axis='y', labelcolor='red')

    plt.xticks(ticks=x, labels=timestamps, rotation=20, size=7)

    ax2 = ax1.twinx()

    ax2.set_ylabel('Place', color='blue')
    ax2.plot(x, rank, color='blue', marker='o')
    ax2.tick_params(axis='y', labelcolor='blue')
    # Invert the y-axis for the first subplot (ax1)
    ax1.invert_yaxis()

    # Convert points and rank to numeric types before using them
    #numeric_points = [float(p) for p in points]
    #numeric_rank = [float(r) for r in rank]

    # Set y-axis ticks as a range from min(points) to max(points)
    #num_ticks = 5  # Adjust the number of ticks as needed
    #ax1.set_yticks(np.linspace(min(numeric_points), max(numeric_points), num_ticks))
    #ax2.set_yticks(np.linspace(min(numeric_rank), max(numeric_rank), num_ticks))
    
    plt.tight_layout()
    plt.savefig('graph.png')

def loadData():
    global timestamps, x, points, rank
    timestamps = []
    x = []
    points = []
    rank = []
    #load data from json
    with open("data.json", "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}
    try:
        for item in data["snapshots"]:
            timestamps.append(item['timestamp'])
            x.append(item['x'])
            points.append(item['points'])
            rank.append(item['rank'])
    except:
        pass
def saveData():
    global timestamps, x, points, rank
    #save data to json
    newSnapshot = {
        "timestamp": timestamps[-1],
        "x": x[-1],
        "points": points[-1],
        "rank": rank[-1]
    }
    data = {}
    with open("data.json", "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}
            data["snapshots"] = []
        data["snapshots"].append(newSnapshot)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def pullData(clan):
    global timestamps, x, points, rank
    if len(x) == 0:
        x.append(1)
    else:
        x.append(x[-1] + 1)
    timestamps.append(datetime.now().strftime("%d-%m-%y\n%H:%M"))
    d = functions.get_clan_output(clan)
    if d == "not existing":
        points.append(0)
        rank.append(0)
    else:
        points.append(d[2])
        rank.append(d[0])
    if len(x) > 10:
        del x[0]
        del points[0]
        del rank[0]
        del timestamps[0]


def task(clan):
    loadData()
    plot(clan)
    sleep_until_next_hour()
    while True:
        print("Generating diagram...")
        loadData()
        pullData(clan)
        saveData()
        plot(clan)
        sl(1 * 60 * 60)

def runTask(clan):
    global t
    t = threading.Thread(target=task, args=(clan,))
    t.start()

