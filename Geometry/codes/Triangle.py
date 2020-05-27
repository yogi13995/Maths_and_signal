import numpy as np
import matplotlib.pyplot as plt
#from coeffs import *
import subprocess
import shlex

#sides of triangle
a = 3
b = 5
c = 6

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
P = np.array([x+5,y])
Q = np.array([5,0])
R = np.array([a+5,0])
N = np.array([(a/2)+5,0])


A = np.array([x,y])
B = np.array([0,0])
C = np.array([a,0])
M = np.array([a/2,0])


#Generating the lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)
x_PN = line_gen(P,N)

#Generating the lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AM = line_gen(A,M)

#plotting the all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_PN[0,:],x_PN[1,:],label='$PN$')


plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1), P[1]*(1-0.1), 'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1), Q[1]*(1), 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0]*(1+0.03), R[1]*(1-0.1),'R')
plt.plot(N[0], N[1], 'o')
plt.text(N[0]*(1+0.03), N[1]*(1-0.1),'N')





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
plt.savefig('Triangle.pdf')

plt.show()
