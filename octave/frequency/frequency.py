import numpy as np
import matplotlib.pyplot as plt
import math

x = np.loadtxt('frequency.dat', dtype = 'double')


A = []
estimate = []
for i in range(0,18):
	A.append(x[i])
	
	
for i in range(0,18):
	estimate.append(x[i+18])
	
	
print(A)
print(estimate)

plt.grid(True, which = "both")
plt.plot(A,estimate)
plt.ylabel('$estimate$')
plt.xlabel('$A$')


plt.savefig('frequency.pdf')
plt.savefig('frequency.eps')


plt.show()
