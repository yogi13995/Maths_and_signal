import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from cvxpy import *

c = np.array([3,2])
A = np.array([[-1,-1], [3,5]])
b = np.array([-8,15])

x = Variable((2,1),nonneg=True)
f = c@x
obj = Minimize(f)
constraints = [A@x <= b]
problem(obj, constraints).solve()
print(f.value, x.value)

