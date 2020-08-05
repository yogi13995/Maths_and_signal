import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from cvxpy import *

c = np.array([5,10])
A = np.array(([-1,-2], [1,1],[1,-2])).T
b = np.array([-120,60,0]).reshape((3,-1))

x = Variable((2,1),nonneg=True)
f = c@x
obj1 = Minimize(f)
obj2 = Maximize(f)
constraints = [A.T@x >= b]
Problem(obj2, constraints).solve()
print(f.value, x.value)
Problem(obj1, constraints).solve()
print(f.value, x.value)

n1 = np.array([1,2])
n2 = np.array([1,1])
n3 = np.array([1,-2])

c1 = 120
c2 = 60
c3 = 0
A=line_intersect(n1,c1,n2,c2)
I=line_intersect(n2,c2,n3,c3)
J=line_intersect(n3,c3,n1,c1)
#print(A)

B,C = line_icepts(n1,c1)
D,F = line_icepts(n2,c2)
a = np.array(range(120))
b  =  a/2

x_BC = line_gen(B,C)
x_DF = line_gen(D,F)



points = np.array([D,I,J,B])


plt.fill(points[:,0], points[:,1], 'k', alpha=0.3)

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 ) , 'A')
plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 + 0.1), I[1] * (1 ) , 'I')
plt.plot(J[0], J[1], 'o')
plt.text(J[0] * (1 + 0.1), J[1] * (1 ) , 'J')
plt.plot(x_BC[0,:],x_BC[1,:],label='$x+2y = 120$')
plt.plot(x_DF[0,:],x_DF[1,:],label='$x+y = 60$')
plt.plot(a,b,label='$x - 2y = 0$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.savefig('../figures/lp9.eps')
plt.show()

