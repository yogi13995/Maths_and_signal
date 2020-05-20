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
A = np.array([x,y])
B = np.array([0,0])
C = np.array([a,0])
M = np.array([a/2,0])

#Generating the lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AM = line_gen(A,M)

#plotting the all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AM[0,:],x_AM[1,:],label='$AM$')

plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1), A[1]*(1-0.1), 'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.2), B[1]*(1), 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1+0.03), C[1]*(1-0.1),'C')
plt.plot(M[0], M[1], 'o')
plt.text(M[0]*(1+0.03), M[1]*(1-0.1),'M')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.show()
