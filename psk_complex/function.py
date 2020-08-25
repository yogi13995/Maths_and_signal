import numpy as np
import matplotlib.pyplot as plt
import math


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
	
