import matplotlib.pyplot as plt
from datetime import datetime
from random import randint

c = 0
#xt = []
x = []
#y = []
#y2 = []

#for i in range(10):
#    c+=1
#    x.append(c)
#    xt.append(datetime.now().strftime("%d-%m-%y"))
#    y.append(randint(1, 10))
#    y2.append(randint(1, 10))

def plot(po, pl, da):
    global c
    global x
    

    c += 1
    x.append(c)
    
    shit, ax1 = plt.subplots()

    ax1.set_xlabel('Date/Time')
    ax1.set_ylabel('Points', color = 'red')
    print(x)
    print(po)
    print(pl)
    print(da)
    ax1.plot(x, po, color = 'red')
    ax1.tick_params(axis ='y', labelcolor = 'red')

    plt.xticks(ticks=x, labels=da, rotation=20, size=8)

    ax2 = ax1.twinx() 

    ax2.set_ylabel('Place', color = 'blue') 
    ax2.plot(x, pl, color = 'blue') 
    ax2.tick_params(axis ='y', labelcolor = 'blue')

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('graph.png')
