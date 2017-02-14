#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 16 de Dezembro de 2016  
    Descricao: esta bilbioteca possui as seguintes funcoes:

		plotGraph: esta funcao recebe dois vetores (x,y), mais um terceiro vetor do desvio padrao, plotando esses valores em um grafico. Com uma lista de parametros, imprime na tela os valores da eficiencia quantica maxima, comprimento de onda com maxima EQ e a procentagem de conversao.

		parametrosGraph: esta funcao recebe uma string do lambda inicial, lambda final e passo utilizado no ensaio, para criar um vetor do espectro de luz. Recebe tambem o vetor dos valores da EQ para realizar uma interpolacao. Essa interpolacao sera usada no calculo da EQmax, Lambda_max e porcentagem de conversao de luz.

		returnMax: dado um vetor, esta funcao retornara seu valor maximo.

    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import matplotlib.pyplot as plt
import numpy as np
import copy

from scipy.interpolate import interp1d, splrep, splev
from scipy.integrate import quad

from QE_reduceImgs_readArq import LeArq_curvaEQFabricante

def plotGraph(x,y, std, parametrosGraph, name):
	FatorConversao = 0
	if name != '':
		EQfabricante, espectroFrabricante = LeArq_curvaEQFabricante(name)
		plt.plot(espectroFrabricante, EQfabricante, c='red',linestyle='--')
		
		CopyY = copy.copy(y) 
		EQmaxDados, LambdaDados = returnMax(CopyY)	

	font = 15	
	plt.plot(x,y, c='blue')
	plt.errorbar(x,y,std, fmt='o', c='blue')
	plt.xlabel(r'$\mathtt{Comprimento \quad de \quad onda \; (nm)}$', size=font)
	plt.ylabel(r'$\mathtt{EQ \quad (}$' + '%' + r'$\mathtt{)}$', size=font)
	plt.title(r'$\mathtt{Curva \quad de \quad Efici\^encia \quad Qu\^antica}$', size=font)
	plt.xlim(xmin=x[0]*0.99, xmax=x[-1])
	plt.ylim(ymin = 0, ymax=100)

	plt.annotate(r'$\mathtt{EQ_{max} \; = \; %.1f}$' %(parametrosGraph[0]) + ' %', xy=(0.62,0.95), xycoords='axes fraction',  ha='left', va='center', size=font)
	plt.annotate(r'$\mathtt{Comp. \; onda \; = \; %.2f \; (nm)}$' %(parametrosGraph[1]), xy=(0.62,0.9), xycoords='axes fraction',  ha='left', va='center', size=font)
	plt.annotate(r'$\mathtt{Convers\~ao \; = \; %.2f}$' %(parametrosGraph[2]) + ' %', xy=(0.62, 0.85), xycoords='axes fraction',  ha='left', va='center', size=font)


def parametrosGraph(string, dados):

	#recebe string no formato 00,00,00
	listValues = string.split(',')
	xInicial = int(listValues[0])
	xFinal	 = int(listValues[1])
	step	 = int(listValues[2])
	n = (xFinal - xInicial)/step
	x = np.linspace(xInicial, xFinal, n+1)
	f = interp1d(x, dados, kind='cubic')
	
	#parametros das imagens
	fmax, i= returnMax(f(x))
	integral = quad(f, x[0],x[-1])
	absPorcent = integral[0]/(x[-1] - x[0])
	parametrosGraph= [fmax, x[i], absPorcent]

	return x, f, parametrosGraph






#retorna valor maximo da curva de EQ
def returnMax(dados):
	i, index = 0, 0
	fvetor = dados
	while i < len(fvetor)-1:
		if fvetor[i] > fvetor[i+1]:
			vartemp = fvetor[i+1]
			fvetor[i+1] = fvetor[i]
			fvetor[i] = vartemp
		else:
			index = i+1
		i+=1
	return fvetor[-1], index

