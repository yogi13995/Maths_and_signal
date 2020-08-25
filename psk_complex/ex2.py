import numpy as np
import matplotlib.pyplot as plt
import math
from function import *

#SNR range
snrlen = 10

#SNR in dB and actual per bit 
#(Check Proakis for factor of 6)
snr_db = np.linspace(0,snrlen,snrlen)
snr = 6.0*10.0**(0.1*snr_db)

#Bitstream size
bitsimlen = 99999
#Symbol stream size
simlen = bitsimlen//3
#Generating bits
bits = np.random.randint(2, size=(1,bitsimlen))


#Converting bits into gray code
s = np.zeros((8,2))
for i in range(0,8):
	s[i,:] = (math.cos((i)*2*math.pi/8), math.sin((i)*2*math.pi/8))



		
symbol_list = symb(bits, simlen, s)
symbol = np.transpose(symbol_list)	
symbol_comp = symbol[0,:]+ 1j*symbol[1,:]

gray = np.zeros((8,3))
gray[0,:] = [0,0,0]
gray[1,:] = [0,0,1]
gray[2,:] = [0,1,1]
gray[3,:] = [0,1,0]
gray[4,:] = [1,1,0]
gray[5,:] = [1,1,1]
gray[6,:] = [1,0,1]
gray[7,:] = [1,0,0]


A = np.zeros((8,2,2))
A[0,:,:] = [[math.sqrt(2)-1, math.sqrt(2)-1], [1, -1]]
A[1,:,:] = [[math.sqrt(2)+1, -math.sqrt(2)+1], [-1, 1]]
A[2,:,:] = [[-math.sqrt(2)-1, math.sqrt(2)+1], [1, 1]]
A[3,:,:] = [[math.sqrt(2)-1, -math.sqrt(2)-1], [1, -1]]
A[4,:,:] = [[-math.sqrt(2)+1, -math.sqrt(2)+1], [-1, 1]]
A[5,:,:] = [[-math.sqrt(2)-1, math.sqrt(2)-1], [1, -1]]
A[6,:,:] = [[math.sqrt(2)+1, -math.sqrt(2)-1], [-1, -1]]
A[7,:,:] = [[-math.sqrt(2)+1, math.sqrt(2)+1],[-1, 1]]


		
ser = []
ser_ana = []
ber = []
	
for k in range(0,snrlen):
	noise_comp = np.random.normal(0, 1, size =(1, simlen)) + 1j*np.random.normal(0, 1, size=(1, simlen))
	y_comp =np.dot(math.sqrt(snr[k]),symbol_comp) + noise_comp
	t = 0
	brx = np.zeros((simlen,3))
	for i in range(0,simlen):
		z = decodecomp(y_comp[0,i],A)
		srx_comp = s[z,:]
		brx[i,:] = gray[z,:]
	
		if (symbol_comp[i].real == srx_comp[0]) and (symbol_comp[i].imag == srx_comp[1]):
			t =t+1
			
	#print(t)		
	ser.append(1 - (t/simlen))
	#print(ser)
	ser_ana.append(2*qfunc(math.sqrt(snr[k])*math.sin(math.pi/8)))
	brx = np.transpose(brx)
	brx = np.reshape(brx,(1,bitsimlen))
	bit_diff = bits-brx
	#print(np.count_nonzero(bit_diff))
	ber.append(np.count_nonzero(bit_diff)/bitsimlen)


#plots
plt.grid(True, which = "both")
plt.semilogy(snr_db, ser_ana, label='SER Analysis')
plt.semilogy(snr_db, ser, 'o', label = 'SER Simulation')
plt.semilogy(snr_db, ber, label = 'BER Simulation')
plt.xlabel('SNR in dB')
plt.ylabel('Error Rate')
plt.legend()
plt.title('BER & SER curve for 8PSK')
plt.savefig('./figs/fig.pdf')
plt.savefig('./figs/fig.eps')
plt.show()



