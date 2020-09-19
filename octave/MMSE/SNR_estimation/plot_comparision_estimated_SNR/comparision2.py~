import numpy as np
import matplotlib.pyplot as plt
import math

x1 = np.loadtxt('MMSE_py1.dat', dtype = 'double')
x2 = np.loadtxt('MMSE_py.dat', dtype = 'double')

EbN01 = np.vstack((x1[0,:]))
SER_MMSE1 = np.vstack((x1[1,:]))

EbN02 = np.vstack((x2[0,:]))
SER_MMSE2 = np.vstack((x2[1,:]))

plt.grid(True, which="both")
plt.semilogy(EbN01, SER_MMSE1, label= 'MMSE_without_estimated_SNR')
plt.semilogy(EbN02, SER_MMSE2, label= 'MMSE_with_estimated_SNR')
plt.xlabel('{E_s}/{N_0}')
plt.ylabel('P_e')
plt.legend()

plt.savefig('./figs/MMSE_oct.pdf')
plt.savefig('./figs/MMSE_oct.eps')

plt.show()
