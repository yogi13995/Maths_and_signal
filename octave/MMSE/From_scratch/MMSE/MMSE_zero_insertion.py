import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
import random
import subprocess
import shlex
from scipy import signal
from scipy.linalg import toeplitz
import scipy
TimeSlot=2e-3 #Transmit time duration
SNR = 1 #Signal to noise ratio
Rs = 123e3 # symbol rate %53.34
#scaling_factor = 10e6;
M=8
#Nf = 5 # MMSE filter length
L = 5 # Channel filter length
#N = 1e4   # Number of symbols
EbN0dB=np.zeros((16,))  # SNR in dB
for i in range(16):
	EbN0dB[i]=i
kk=math.log2(M)
EsN0dB =np.zeros((16,))
for i in range(16):
	 EsN0dB[i]=EbN0dB[i]+10*math.log10(kk) # Adding 3 dB to SNR as we are calculating Symbol Error Rate

nFrames = 1000
len_frame1 = 240*3
len_frame = (len_frame1/3)
len_pilot1 = 3*10
len_pilot=(len_pilot1/3)
len_seq1=3*4
len_seq = (len_seq1/3)
N = (len_frame)*nFrames/2
#
DataSym =np.zeros((len_pilot1,1))
for ia in range(len_pilot1):
	DataSym[ia]=(random.randint(0,1))

DataSym1=np.reshape(DataSym,(3,10))
DataSym2=np.transpose(DataSym1)
DataSym3=np.zeros((int(len_pilot),))

for ii in range(int(len_pilot)):
	DataSym3[ii]=4*DataSym2[ii,0]+2*DataSym2[ii,1]+DataSym2[ii,2]+1
# mapping function
def mapping(M,dataSym):
	I=np.cos((dataSym-1)/M*2*np.pi)
	Q=np.sin((dataSym-1)/M*2*np.pi)
	m_psk=(I+1j*Q)
	return m_psk

pilot_sym =mapping(M,DataSym3.reshape(-1,1))   # 8-PSK modulation
#nErr_seq = zeros(1,length(EsN0dB));
SER_MMSE=np.zeros(len(EsN0dB),)


#function y_ind=demapping(M,rx)
def demapping(M,rx):
#	%M=8;
	received=rx
	s_i=np.zeros((1,M))
	s_q=np.zeros((1,M))
	for ja in range(M):
		s_i[0][ja]=np.cos(ja/M*2*np.pi)
		s_q[0][ja]=np.sin(ja/M*2*np.pi)
	y_ind = np.zeros((1, len(rx)))
	for iter in range(len(rx)):
		min_dist = 2147483647
		min_dist_ind = 0
		for iter2 in range(M):
			real_dist = (s_i[0][iter2] - abs(rx[iter].real))**2
			imag_dist = (s_q[0][iter2]- abs(rx[iter].imag))**2
			total_dist = real_dist + imag_dist
			if(total_dist < min_dist):
				min_dist = total_dist
				min_dist_ind = iter2
		y_ind[0][iter] = min_dist_ind
	return y_ind
#function h_hat = Channel_estimatiom(x_p,y_p,L)
def channel_Estimation_fft(x_p,y_p,L):
    scaling_factor = 10e6
    z_p =np.flip(y_p)
    y_p[0:L-1] = y_p[0:L-1]+np.flip(z_p[0:L-1])
    y = y_p[0:len(y_p)-L+1]
    X = np.fft.fft(x_p)
    Y=np.fft.fft(y)*scaling_factor
    H = np.divide(Y,X)
    h_hat = np.fft.ifft(H)
    return h_hat

def MMSE_matrix(h,l,snr):
	zer=np.zeros((int(l-len(h)),1)).reshape(-1,1)
	hr=np.array([h[1],0,0,0]).reshape(-1,1)
	hc=np.concatenate((h,zer),axis=0)
	H=toeplitz(hc,hr)
	Ain=(np.matmul(np.transpose(H),H)+(np.eye(4,4))/snr)
	Ain=Ain.astype('complex128')
	w=np.matmul(np.linalg.inv(Ain),np.transpose(H))
	return w

def zero_padding(x):
	y=np.array([])
	y = np.hstack(((x[0,0:4]).reshape(1,-1),np.zeros((1,4)))).reshape(1,-1)
	for ib in range(2,(int(len(x[0])/4)+1)):
		y = np.hstack((y.reshape(1,-1),(x[0,(ib-1)*4:(ib-1)*4+4]).reshape(1,-1),np.zeros((1,4)))).reshape(1,-1)
	return y
SER_MMSE=[]
for i in range(len(EsN0dB)):
	nErr_mmse = 0
	EsN01in=10**(EsN0dB[i]/10)
	for j in range(nFrames):
		h1 = (np.random.randn(L-1,1)).reshape(-1,1)
		h2 = (np.random.randn(L-1,1)).reshape(-1,1)
		h  = h1 + 1j*h2
		h = h/math.sqrt(2)
		h = np.concatenate(((np.array([1])).reshape(-1,1),h),axis=0)                 # Rician fading channel
		h = h/math.sqrt(L)
		# Channel estimation
		Rk_p = (np.convolve(np.ndarray.flatten(h),np.ndarray.flatten(pilot_sym))).reshape(-1,1)
		noiseSigma=1/math.sqrt(2)*math.sqrt(1/(2*EsN01in))
		noise=noiseSigma*((np.random.randn(len(Rk_p),1)).reshape(-1,1)+1j*(np.random.randn(len(Rk_p),1)).reshape(-1,1))
		y_p = Rk_p + noise
		h_hat = channel_Estimation_fft(pilot_sym,y_p,L)
		h_est = h_hat[0:L]
		w = MMSE_matrix(h_est,len(h)+len_seq-1,EsN01in)
		#for k=1:len_frame
		DataSym =np.zeros((int(len_frame1/2),1))
		for ic in range(int(len_frame1/2)):
			DataSym[ic]=(random.randint(0,1))
		DataSym1=np.reshape(DataSym,(3,int(len_frame1/6)))
		DataSym2=np.transpose(DataSym1)
		DataSym3=np.zeros(int(len_frame/2),)
		for ii in range(int(len_frame/2)):
			DataSym3[ii]=4*DataSym2[ii,0]+2*DataSym2[ii,1]+DataSym2[ii,2]+1
		m_psk = (mapping(M,(DataSym3).reshape(-1,1))).reshape(1,-1)
		m_psk1 = zero_padding(m_psk)
		Rk = np.convolve(np.ndarray.flatten(h),np.ndarray.flatten(m_psk1)).reshape(-1,1)
		Rk1 = Rk.reshape((244,1))
		#Rk=m_psk
		noiseSigma=1/math.sqrt(2)*math.sqrt(1/(2*EsN01in))
		noise=noiseSigma*(np.random.randn(len(Rk),1).reshape(-1,1)+1j*np.random.randn(len(Rk),1)).reshape(-1,1)
		y = Rk1 + noise    # Received symbols with AWGN noise
##################################################################################################################
		# MMSE Equalizer
		y1 = y[0:8,0].reshape(-1,1)
		x_hat = np.matmul(w,y1)
		x_hat1=demapping(M,x_hat)
		x_hat2=(x_hat1-1)
		xdb=x_hat2
		x_hat3=np.zeros((4,3))
		for dec in range(4):
			x_hat3[dec,2]=xdb[0,dec]%2
			x_hat3[dec,1]=(int(xdb[0,dec]/2))%2
			x_hat3[dec,0]=(int(xdb[0,dec]/4))%2
		x_hat4=np.transpose(x_hat3)
		x_hat5=x_hat4.reshape(-1,1)
		X_hat = x_hat5.reshape(-1,1)
		#X_hat=np.empty(())
		nErr_frame = 0
		for jj in range(2,(int(len_frame/8)+1)):
			y1 = y[(jj-1)*8:(jj-1)*8+8,0].reshape(-1,1)
			x_hat = np.matmul(w,y1)
			x_hat1=demapping(M,x_hat)
			x_hat2=(x_hat1-1)
			xdb=x_hat2
			x_hat3=np.zeros((4,3))
			for dec in range(4):
				x_hat3[dec,2]=xdb[0,dec]%2
				x_hat3[dec,1]=(int(xdb[0,dec]/2))%2
				x_hat3[dec,0]=(int(xdb[0,dec]/4))%2
			x_hat4=np.transpose(x_hat3)
			x_hat5=x_hat4.reshape(-1,1)
			X_hat = np.concatenate((X_hat,x_hat5),axis=0).reshape(-1,1)
               #  disp(size(X_hat))
                 #nErr_frame = nErr_frame + sum(DataSym((jj-1)*4*3+1:(jj-1)*4*3+12)~=x_hat5);
		#print(j)
		nErr_mmse = nErr_mmse + sum(DataSym!=X_hat)
		#nErr_mmse = nErr_mmse + nErr_frame; 
	SER_MMSE.append(nErr_mmse/(3*N))
	print(i)
	print("-------------------------------")

EbN0=np.zeros((len(EbN0dB,)))
for i in range(len(EbN0dB)):
	EbN0=10**(EbN0dB[i]/10)
theoreticalSER=(1/kk)*(math.erfc(math.sqrt(EbN0*math.log2(M))*np.sin(np.pi/M)))
theory_bpsk = 1.0/2* math.erfc(math.sqrt(EbN0))

# Plots
plt.semilogy(EbN0dB,(SER_MMSE))
plt.title("MMSE")
plt.xlabel("Es/N0 (dB)")
plt.ylabel("Pe")
plt.grid()

##if using termux
plt.savefig('./figs/mmse_ser.pdf')
plt.savefig('./figs/mmse_ser.eps')
subprocess.run(shlex.split("termux-open ./figs/mmse_ser.pdf"))
#else
#plt.show()


