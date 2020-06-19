import numpy as np
import matplotlib.pyplot as plt
import math
#from coeffs import *
import subprocess
import shlex



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
P = np.array([2,1])
Q= np.array([-2,3])
R = np.array([4, 5])
S = np.array([0, 2])



#Generating the lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)
x_RS = line_gen(R,S)

#plotting the all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_RS[0,:],x_RS[1,:],label='$RS$')



plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1 + 0.1), P[1]*(1-0.2), 'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1), Q[1]*(1-0.1), 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0]*(1+0.03), R[1]*(1-0.1),'R')
plt.plot(S[0], S[1], 'o')
plt.text(S[0]*(1), S[1]*(1-0.2),'S')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('../figures/triangle/triangle.eps')

plt.show()
