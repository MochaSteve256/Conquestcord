# Import Library

import matplotlib.pyplot as plt
from datetime import datetime
from random import randint
# Define Data
c = 0
xt = []
x = []
y = []
for i in range(10):
    c+=1
    x.append(c)
    xt.append(datetime.now().strftime("%d-%m-%y"))
    y.append(randint(1, 10))
# Plot
plt.xticks(ticks=x, labels=xt, rotation=20, size=7)
plt.plot(x, y, color='r')
plt.xlabel("Date/Time")
plt.ylabel("Points")
# Save image as png

plt.savefig('save.png')
