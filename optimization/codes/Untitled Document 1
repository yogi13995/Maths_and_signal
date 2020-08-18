import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from cvxpy import *

c = np.array([-3,4])
A = np.array(([1,2], [3,2])).T
b = np.array([8,12]).reshape((2,-1))

x = Variable((2,1),nonneg=True)
f = c@x
obj = Minimize(f)
constraints = [A.T@x <= b]
Problem(obj, constraints).solve()
print(f.value, x.value)

n1 = np.array([1,2])
n2 = np.array([3,2])

c1 = 8
c2 = 12

A=line_intersect(n1,c1,n2,c2)
print(A)

B,C = line_icepts(n1,c1)
D,F = line_icepts(n2,c2)

x_BC = line_gen(B,C)
x_DF = line_gen(D,F)


points = np.array([[0,0],C,A,D])


plt.fill(points[:,0], points[:,1], 'k', alpha=0.3)

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 ) , 'A')
plt.plot(x_BC[0,:],x_BC[1,:],label='$x+2y = 8$')
plt.plot(x_DF[0,:],x_DF[1,:],label='$3x +2y  = 12$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 



plt.savefig('../figures/lp4.eps')
plt.show()

