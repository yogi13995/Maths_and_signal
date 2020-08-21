from __future__ import division
import random
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import cmath


#if using termux
import subprocess
import shlex
#end if

from qfunc import qfunc
from bs import bitstream
from mapping import mapping

bits = []
bits = bitstream(100000)
symbol =[]

for i in range(0,bits.size-2,3):
	b0 = bits[i];
	b1 = bits[i+1];
	b2 = bits[i+2];
	symbol.append(mapping(b0,b1,b2))


b0 =bits[len(bits)-1]
b1 =0
b2 =0

symbol.append(mapping(b0,b1,b2))
snr_db = np.linspace(0,9,10)
snrlen=10

err =[]

print(len(symbol))

s_in,s_q =0,0
ber=[]
for k in range(0,snrlen):
	snr = 10**(0.1*snr_db[k])
	received = []
	t=0
	for i in range(len(symbol)):
		if symbol[i] == "s0":
			s_in = 1
			s_q = 0
		elif symbol[i] =="s1":
			s_in = 1/np.sqrt(2)
			s_q = 1/np.sqrt(2)
		elif symbol[i] == "s2":
			s_in = 0
			s_q = 1
		elif symbol[i] == "s3":
			s_in = -1/np.sqrt(2)
			s_q = 1/np.sqrt(2)
		elif symbol[i]=="s4":
			s_in=-1
			s_q=0
		elif symbol[i]=="s5":
			s_in=-1/np.sqrt(2)
			s_q=-1/np.sqrt(2)
		elif symbol[i]=="s6":
			s_in=0
			s_q=-1
		elif symbol[i]=="s7":
			s_in=1/np.sqrt(2)
			s_q=-1/np.sqrt(2)
		noise1 = np.random.normal(0,1,1)
		noise2 = np.random.normal(0,1,1)

		y1 = mp.sqrt(snr)*s_in + noise1
		y2 = mp.sqrt(snr)*s_q + noise2



		if(y1+(np.sqrt(2)-1)*y2>0 and y2-(np.sqrt(2)-1)*y1<0):

			received.append("s0")



		elif(y2-(np.sqrt(2)-1)*y1>0 and y2-(np.sqrt(2)+1)*y1<0):

			received.append("s1")


		elif(y2-(np.sqrt(2)+1)*y1>0 and y2+(np.sqrt(2)+1)*y1>0):

			received.append("s2")


		elif(y2+(np.sqrt(2)-1)*y1>0 and y2+(np.sqrt(2)+1)*y1<0):
			received.append("s3")

		elif(y2+(np.sqrt(2)-1)*y1<0 and y2-(np.sqrt(2)-1)*y1>0):
			received.append("s4")
		elif(y2-(np.sqrt(2)+1)*y1>0 and y2-(np.sqrt(2)-1)*y1<0):
			received.append("s5")
		elif(y2-(np.sqrt(2)+1)*y1<0 and y2+(np.sqrt(2)+1)*y1<0):
			received.append("s6")
		elif(y2+(np.sqrt(2)-1)*y1<0 and y2+(np.sqrt(2)+1)*y1>0):
			received.append("s7")
		
		if symbol[i]==received[i]:
			t+=1;

	err.append(1-(t/33334.0))
	ber.append((qfunc(mp.sqrt((0.142*snr))))*2)

plt.semilogy(snr_db.T,ber,label='Analysis')
plt.semilogy(snr_db.T,err,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11012.pdf')
plt.savefig('./figs/ee18btech11012_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11012.pdf")
#else

plt.show()
