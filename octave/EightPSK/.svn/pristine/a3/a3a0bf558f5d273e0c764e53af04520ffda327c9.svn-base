from __future__ import division
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#the ber expression is sqrt(E_b)+n1-n2<0

def qfunc(x):
	return 0.5*mp.erfc(x/np.sqrt(2))

#Number of SNR samples 
snrlen = 10
#SNR values in dB
snrdb = np.linspace(8,17,10)
#Number of samples
simlen = int(0.5e5)
#Simulated BER declaration		
err = []
corr=[]
#Analytical BER declaration
ber = []
temp=0
noise1 = np.random.normal(0,1,simlen)
noise2=np.random.normal(0,1,simlen)
M=8
cons=np.tan(np.pi/M)
cons1=1+(1/cons)**2
#for SNR 0 to 10 dB
for i in range(0,snrlen):
		#Generating AWGN, 0 mean unit variance
		#from dB to actual SNR
		snr = 10**(0.1*snrdb[i])	#Received symbol in baseband
		rx = mp.sqrt(6*snr) + noise1
		ry = noise2
		#storing the index for the received symbol 
		#in error
		temp=0
		for j in range (0,len(rx)):
		    if ((cons*rx[j]>ry[j]) and (cons*rx[j]>-ry[j])):
		    	temp=temp+1                
                				
		#calculating the total number of errors
		#calcuating the simulated BER
		corr.append(temp/simlen)
		err.append(1-(temp/simlen))
		#calculating the analytical BER
		ber.append((qfunc(mp.sqrt((6*snr)/(cons1))))*2)

#the below two lines plot the probability of incorrectly decoding the transmitted symbol
plt.semilogy(snrdb.T,ber,label='Analysis')
plt.semilogy(snrdb.T,err,'o',label='Sim')
#plt.semilogy(snrdb.T,corr,label='P(correct)') #uncomment this line to get the probability of correctly decoding the transmitted symbol
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.title('P_e')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11012.pdf')
plt.savefig('./figs/ee18btech11012.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11012.pdf"))
#else

#plt.show()
