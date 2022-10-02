# Import Library

import matplotlib.pyplot as plt

# Define Data

x= [1, 2, 3, 4, 5]
y= [2.5, 6.3, 12, 14, 2]

# Plot 

plt.plot(x,y,color='r')
plt.xlabel("Date/Time")
plt.ylabel("Points")
# Save image as png

plt.savefig('save.png')
