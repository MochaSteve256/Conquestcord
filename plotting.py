import matplotlib.pyplot as plt
from datetime import datetime
from time import sleep as sl

import threading
import functions

timestamps = []
x = []
points = []
rank = []

def plot(clan):
    shit, ax1 = plt.subplots()
    del shit
    plt.title(clan)

    ax1.set_xlabel('Date/Time')
    ax1.set_ylabel('Points', color = 'red')
    ax1.plot(x, points, color = 'red')
    ax1.tick_params(axis ='y', labelcolor = 'red')

    plt.xticks(ticks=x, labels=timestamps, rotation=20, size=7)

    ax2 = ax1.twinx()

    ax2.set_ylabel('Place', color = 'blue') 
    ax2.plot(x, rank, color = 'blue') 
    ax2.tick_params(axis ='y', labelcolor = 'blue')

    plt.gca().invert_yaxis()
    plt.savefig('graph.png')

def pullData(clan):
    global timestamps, x, points, rank
    if len(x) == 0:
        x.append(1)
    else:
        x.append(x[-1] + 1)
    timestamps.append(datetime.now().strftime("%d-%m-%y"))
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
    while True:
        pullData(clan)
        plot(clan)
        sl(24 * 60 * 60)
        #sl(1)

def runTask(clan):
    global t
    t = threading.Thread(target=task, args=(clan,))
    t.start()
runTask("KANHNI")