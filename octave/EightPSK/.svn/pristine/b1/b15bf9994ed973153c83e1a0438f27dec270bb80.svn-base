import numpy as np
import mpmath as mp
from bs import bitstream
from mapping import mapping

def symb():
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
	print(len(symbol))
	return symbol

snr_db = np.linspace(0,9,10)
snrlen=10

err =[]




