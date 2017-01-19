#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 10 de Outubro de 2016  
    Descricao: este modulo tem como entrada uma serie de dados da FFT, assim como a posicao neste vetor de cada um dos picos. Retorna um vetor com a probabilidade de cada um dos picos nao ser um sinal verdadeiro. Essa probabilidade e calculada pela integracao de curva normal para e media e desvio padrao dos dados, desde o ponto do valor do pico até o valor da media+3sgimas. 
    
    Laboratorio Nacional de Astrofisica, Brazil.    
"""
__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


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
