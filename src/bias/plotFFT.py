#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 10 de Agosto de 2016  
    Descricao: este modulo tem como entrada dois vetores (x,y) dos dados FFT e dois vetores (xs,ys) dos dados do sinal que servira de referencia, retornando um grafico com ambas as curvas. Este modulo tambem faz uso de uma biblioteca chamada detect_peaks, responsavel por retornar a posicao dos picos acima de um dados limite inferior e a quantidade de picos encontrada.
    
    Laboratorio Nacional de Astrofisica, Brazil.    
"""
__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


import numpy as np
import matplotlib.pyplot as plt
from detect_peaks import detect_peaks

# plota grafico da FFT dos dados e sinal de referencia
def plotFFT(x,y,xs,ys):	
	ax2 = plt.subplot2grid((2,3),(1,0),colspan=2)
	font = 15
	meanY = np.mean(y)
	meanYS = np.mean(ys)	
	stdYS = np.std(ys)


	picos = detect_peaks(y,threshold = meanYS+3*stdYS )
	npicos = range(len(picos))
	if npicos == 0:
		picos = 0


	if npicos != 0:
		for i in npicos:
			plt.text(x[picos[i]]+0.005,y[picos[i]], r'$\mathtt{%i}$' %(i+1),  ha='left', va='center', size=17)

	plt.plot(x,y,'o-',c='blue',label= r'$\mathtt{FFT \; dos \; dados}$')
	plt.plot(xs,ys, c='red', label = r'$\mathtt{FFT \; refer\^encia}$')
	plt.xlabel(r'$\mathtt{Frequ\^encia \;\; (Hz)}$',fontsize = font)
	plt.ylabel(r'$\mathtt{Contagens \;\; (adu)}$', fontsize = font)
	plt.title(r'$\mathtt{Transformada \;\; de \;\; Fourier \;\; da \;\; corrente \;\; de \;\; escuro}$', fontsize = font)
	plt.legend(loc = 'lower left')



	return picos, npicos
