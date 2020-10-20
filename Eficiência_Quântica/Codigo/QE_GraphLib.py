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
import copy, os

from scipy.interpolate import interp1d, splrep, splev
from scipy.integrate import quad
from math import sqrt

from QE_reduceImgs_readArq import LeArq_curvaEQFabricante

def plotGraph(x,y, std, parametrosGraph, name, images_path):	

	errorSourceEstabilization = 0.07714 #erro calculado para estabilizacao da fonte
	comprimentoOnda = range(300,1200,100)
	errorPlanAlignment = [0.0, 0.00693, 0.01726, 0.02870, 0.03922, 0.04652, 0.06385, 0.07628, 0.05585]
	Interpolation = interp1d(comprimentoOnda, errorPlanAlignment, kind='cubic')
	ErroExperimental = []
	for Lambda in x:
		ErroExperimental.append(sqrt((Interpolation(Lambda)**2 + errorSourceEstabilization**2)*100**2))

	if name != '':
		EQfabricante, espectroFrabricante = LeArq_curvaEQFabricante(name, images_path)
		plt.plot(espectroFrabricante, EQfabricante,'-', c='green', linewidth=2, label=r'$\mathtt{Fabricante}$')		

	CopyY = copy.copy(y) 
	EQmaxDados, LambdaDados = returnMax(CopyY)	
	x,y,ErroExperimental = np.asarray(x), np.asarray(y), np.asarray(ErroExperimental)

	font = 15	
	plt.plot(x,y, c='blue', label=r'$\mathtt{EQ_{medida}}$')
	plt.errorbar(x,y,std, fmt='o', c='blue')
	plt.plot(x, y - ErroExperimental , c='red',linestyle='--')
	plt.plot(x, y + ErroExperimental , c='red',linestyle='--')

	plt.xlabel(r'$\mathtt{Comprimento \quad de \quad onda \; (nm)}$', size=font)
	plt.ylabel(r'$\mathtt{EQ \quad (}$' + '%' + r'$\mathtt{)}$', size=font)
	plt.title(r'$\mathtt{Curva \quad de \quad Efici\^encia \quad Qu\^antica}$', size=font)
	plt.xlim(xmin=x[0]*0.99, xmax=x[-1])
	plt.ylim(ymin = 0, ymax=100)
	plt.legend(loc='lower left')

	plt.annotate(r'$\mathtt{EQ_{max} \; = \; %.1f}$' %(parametrosGraph[0]) + ' %', xy=(0.32,0.15), xycoords='axes fraction',  ha='left', va='center', size=font)
	plt.annotate(r'$\mathtt{Comp. \; onda \; = \; %.2f \; (nm)}$' %(parametrosGraph[1]), xy=(0.32,0.10), xycoords='axes fraction',  ha='left', va='center', size=font)
	plt.annotate(r'$\mathtt{EQ_{eff} \; = \; %.2f}$' %(parametrosGraph[2]) + ' %', xy=(0.32, 0.05), xycoords='axes fraction',  ha='left', va='center', size=font)		
	
	plt.savefig(images_path + '\\' + 'Relatório EQ.pdf', format='pdf')
	


def parametrosGraph(string, dados):

	#recebe string no formato 00,00,00
	listValues = string.split(',')
	xInicial = int(listValues[0])
	xFinal	 = int(listValues[1])
	step	 = int(listValues[2])
	n = int((xFinal - xInicial)/step)
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

