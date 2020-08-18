import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from cvxpy import *

c = np.array([3,4])
A = np.array(([1,1])).T
b = np.array([4]).reshape((1,-1))

x = Variable((2,1),nonneg=True)
f = c@x
obj = Maximize(f)
constraints = [A.T@x <= b]
Problem(obj, constraints).solve()
print(f.value, x.value)

n1 = np.array([1, 1])

c1 = 4

#A=line_intersect(n1,c1,n2,c2)

B,C = line_icepts(n1,c1)


x_BC = line_gen(B,C)


points = np.array(([0,0],B,C))


plt.fill(points[:,0], points[:,1], 'k', alpha=0.3)

#plt.plot(A[0], A[1], 'o')
#plt.text(A[0] * (1 + 0.1), A[1] * (1 ) , 'A')
plt.plot(x_BC[0,:],x_BC[1,:],label='$x +y = 4$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 



plt.savefig('../figures/lp3.eps')
plt.show()

