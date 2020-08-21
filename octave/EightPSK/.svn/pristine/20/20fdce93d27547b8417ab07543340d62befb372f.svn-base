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
from symbol import symb
from received import rec

err=[]
ber=[]
snr_db=[]
err,ber,snr_db=rec()


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




