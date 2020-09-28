import numpy as np
import matplotlib.pyplot as plt
import math

x1 = np.loadtxt('frequency1.dat', dtype = 'double')
x2 = np.loadtxt('frequency.dat', dtype = 'double')

A1= []
estimate1 = []
for i in range(0,18):
	A1.append(x1[i])
	
	
for i in range(0,18):
	estimate1.append(x1[i+18])
	
A2= []
estimate2 = []
for i in range(0,50):
	A2.append(x2[i])
	
	
for i in range(0,50):
	estimate2.append(x2[i+50])
	
	


plt.grid(True, which = "both")
plt.plot(A1,estimate1, label= 'with pilot = 18,delf = 5e6')
plt.plot(A2,estimate2, label= 'with pilot = 50,delf = 5e4')
plt.ylabel('$estimate$')
plt.xlabel('$A$')
plt.legend()

plt.savefig('frequency.pdf')
plt.savefig('frequency.eps')


plt.show()
