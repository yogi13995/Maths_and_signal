import numpy as np
import matplotlib.pyplot as plt
#from coeffs import *
import subprocess
import shlex

#sides of triangle
a = 3
b = 5
c = 4

#coordinates of A
x=(a**2 + c**2 -b**2)/(2*a)
y=np.sqrt(c**2-x**2)

#generating the line points
def line_gen(A,B):
	len = 20
	dim = A.shape[0]
	x_AB = np.zeros((dim,len))
	lam_1 = np.linspace(0,1,len)
	for i in range(len):
		temp1 = A + lam_1[i]*(B-A)
		x_AB[:,i]=temp1.T
	return x_AB

#vertices
P = np.array([x,y])
Q = np.array([0,0])
R = np.array([a,0])
N = np.array([a/2,0])

#Generating the lines
x_AB = line_gen(P,Q)
x_BC = line_gen(Q,R)
x_CA = line_gen(R,P)
x_AM = line_gen(P,N)

#plotting the all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$PQ$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$RS$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$SP$')
plt.plot(x_AM[0,:],x_AM[1,:],label='$PN$')

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.1), P[1]*(1-0.1), 'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1-0.2), Q[1]*(1), 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0]*(1+0.03), R[1]*(1-0.1),'R')
plt.plot(N[0], N[1], 'o')
plt.text(N[0]*(1+0.03), N[1]*(1-0.1),'N')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.show()
