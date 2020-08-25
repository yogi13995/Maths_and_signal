import numpy as np
import matplotlib.pyplot as plt
import math

snrlen = 10
snr_db = np.linspace(0,snrlen,snrlen)
snr = 6.0*10.0**(0.1*snr_db)
bitsimlen = 99999
simlen = bitsimlen//3

bits = np.random.randint(2, size=(1,bitsimlen))



s = np.zeros((8,2))
for i in range(0,8):
	s[i,:] = (math.cos((i)*2*math.pi/8), math.sin((i)*2*math.pi/8))


def mapping(b0,b1,b2,s):
	if b0 == 0 and b1 == 0 and b2 == 0:
		return s[0,:]
	elif b0 ==0 and b1 == 0 and b2 == 1:
		return s[1,:]
	elif b0 == 0 and b1 == 1 and b2 == 1:
		return s[2,:]
	elif b0 == 0 and b1 == 1 and b2 == 0:
		return s[3,:]
	elif b0 == 1 and b1 == 1 and b2 == 0:
		return s[4,:]
	elif b0 == 1 and b1 == 1 and b2 == 1:
		return s[5,:]
	elif b0 == 1 and b1 == 0 and b2 == 1:
		return s[6,:]
	elif b0 == 1 and b1 == 0 and b2 == 0:
		return s[7,:]



def symb(bits,simlen,s):
	i=0
	symbol = np.zeros((simlen,2))
	for k in range(i,simlen):
		map1 = mapping(bits[0,i],bits[0,i+1],bits[0,i+2],s)
		symbol[k,:]=map1
		i = i+3
	return symbol
	
def decodecomp(vec_comp, A):
	vec = np.zeros((2, 1))
	#print(vec_comp)
	vec[0,0] = vec_comp.real
	vec[1, 0] = vec_comp.imag
	for i in range(0,8):
		y1 = np.matmul([A[i, :, 0],A[i, :, 1]],vec)
		if (y1[0,0] >=0 and y1[1,0] >=0):
			y=i
			return y

def qfunc(x):
	y = 0.5*math.erfc(x/math.sqrt(2))
	return y
	
		
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



