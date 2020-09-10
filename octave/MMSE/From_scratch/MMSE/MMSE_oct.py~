import numpy as np
import matplotlib.pyplot as plt
import math

x = np.loadtxt('MMSE_py.dat', dtype = 'double')

EbN0 = np.vstack((x[0,:]))
SER_MMSE = np.vstack((x[1,:]))

plt.grid(True, which="both")
plt.semilogy(EbN0, SER_MMSE, label= 'MMSE')
plt.xlabel('{E_s}/{N_0}')
plt.ylabel('P_e')
plt.legend()

plt.savefig('./figs/MMSE_oct.pdf')
plt.savefig('./figs/MMSE_oct.eps')

plt.show()
