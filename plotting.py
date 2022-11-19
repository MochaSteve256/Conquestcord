import matplotlib.pyplot as plt
from datetime import datetime
from random import randint

c = 0
xt = []
x = []
y = []
y2 = []

for i in range(10):
    c+=1
    x.append(c)
    xt.append(datetime.now().strftime("%d-%m-%y"))
    y.append(randint(1, 10))
    y2.append(randint(1, 10))
    
shit, ax1 = plt.subplots()

ax1.set_xlabel('Date/Time')
ax1.set_ylabel('Points', color = 'red')
ax1.plot(x, y, color = 'red')
ax1.tick_params(axis ='y', labelcolor = 'red')

plt.xticks(ticks=x, labels=xt, rotation=20, size=7)

ax2 = ax1.twinx() 

ax2.set_ylabel('Place', color = 'blue') 
ax2.plot(x, y2, color = 'blue') 
ax2.tick_params(axis ='y', labelcolor = 'blue')

plt.gca().invert_yaxis()
plt.savefig('graph.png')