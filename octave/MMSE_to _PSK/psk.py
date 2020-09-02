import numpy as np
import matplotlib.pyplot as plt
import math



x = np.loadtxt('psk.dat',dtype='double')

snr_db = np.vstack((x[0,:]))
ser_ana = np.vstack((x[1,:]))
ser = np.vstack((x[2,:]))
ber = np.vstack((x[3,:]))
print(ser_ana)

plt.grid(True, which = "both")
plt.semilogy(snr_db, ser_ana, label='SER Analysis')
plt.semilogy(snr_db, ser, 'o', label = 'SER Simulation')
plt.semilogy(snr_db, ber, label = 'BER Simulation')
plt.xlabel('SNR in dB')
plt.ylabel('Error Rate')
plt.legend()
plt.title('BER & SER curve for 8PSK')

plt.savefig('./figs/psk.pdf')
plt.savefig('./figs/psk.eps')

plt.show()

