# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Create the vectors X and Y
x = np.linspace(-5,5,300)
y = x ** 2 - 15

P1= np.array([3.87, 0])
Q1 = np.array([-3.87, 0])
plt.plot(P1[0],P1[1],'o')
plt.text(P1[0]*(1+0.1), P1[1]*(1-0.1), '\u03B1')
plt.plot(Q1[0],Q1[1],'o')
plt.text(Q1[0]*(1-0.2), Q1[1]*(1), '\u03B2')

# Create the plot
plt.plot(x,y,label='y =t^2 - 15')

# Add a title
plt.title('')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')

# Add a Legend
plt.legend()
plt.savefig('../../figures/conics/perabola4.eps')
# Show the plot
plt.show()
