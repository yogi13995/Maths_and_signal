import numpy as np
import matplotlib.pyplot as plt
import math

x1 = np.loadtxt('MMSE_py1.dat', dtype = 'double')
x2 = np.loadtxt('MMSE_py2.dat', dtype = 'double')

EbN01 = np.vstack((x1))
SER_MMSE1 = np.vstack((x2[:,0]))
SER_MMSE2 = np.vstack((x2[:,1]))
SER_MMSE3 = np.vstack((x2[:,2]))
SER_MMSE4 = np.vstack((x2[:,3]))
SER_MMSE5 = np.vstack((x2[:,4]))


plt.grid(True, which="both")
plt.semilogy(EbN01, SER_MMSE1, label= 'MMSE')
plt.semilogy(EbN01, SER_MMSE2, label= 'MMSE_at_100KHz')
plt.semilogy(EbN01, SER_MMSE3, label= 'MMSE_at_200KHz')
plt.semilogy(EbN01, SER_MMSE4, label= 'MMSE_at_300KHz')
plt.semilogy(EbN01, SER_MMSE5, label= 'MMSE_at_400KHz')
plt.xlabel('{E_s}/{N_0}')
plt.ylabel('P_e')
plt.legend()

plt.savefig('./figs/MMSE_oct.pdf')
plt.savefig('./figs/MMSE_oct.eps')

plt.show()
