import numpy as np
import scipy.integrate as integrate
from math import sqrt
from scipy.integrate import quad

# retorna vetor com probabilidades de cada pico
def probPico(sinalf, picos):
	vetorProb = []	
	mean = np.mean(sinalf)
	std = np.std(sinalf)
	npicos = range(len(picos))
	x = np.linspace((mean-7*std), (mean+7*std), 100)	
	def f(x, mean=mean, std=std):
		f = 1/(sqrt(2*np.pi*std**2))*np.e**(-(x-mean)**2/(2*std**2))
		return f

	for i in npicos:
		vetorProb.append(integrate.quad(f,mean+3*std,sinalf[picos[i]-1])[0])
		
	return vetorProb
