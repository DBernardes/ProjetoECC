#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
	Descricao: esta biblioteca possui as seguintes funcoes:
		Graph_sinal_variance: esta funcao recebe os vetores dos eixos x e y do grafico, assim como o desvio padrao para os eixos X e Y, plotando esses dados. Sobre esses dados realiza um ajuste linear, usado para o calculo do ganho do CCD atraves do coeficiente angular da curva.

		Graph_residuos: esta funcao recebe os valores de X, Y e desvio padrao dos dados, plotando um grafico desses dados subtraidos dos valores do ajuste linear calculado. Faz as marcacoes no grafico das linhas da media e media +/- desvio padrao do resultado da operacao (expressando esses valores na forma literal), para isso utiliza da biblioteca linhaReferencia.
		
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import matplotlib.pyplot as plt
import numpy as np

from scipy import stats
from math import sqrt
from linhaReferencia import linhaReferencia
from algarismoSig import algarismoSig


def Graph_sinal_variance(X, Y, yerr, xerr):
	font = 17	
	global coefAng, intercept, stdLinAjust
	coefAng, intercept, r, p, stdLinAjust = stats.linregress(X,Y)
	ajust = np.poly1d((coefAng,intercept))
	readNoise, stdReadNoise = sqrt(-intercept*coefAng), sqrt(stdLinAjust*coefAng)
	
	ax = plt.subplot(121)
	plt.plot(X, Y, '-', c='blue')	
	plt.errorbar(X,Y,yerr, xerr, fmt='o', c='blue')
	plt.plot(X, ajust(X), c='red')	
	plt.xlabel(r'$\mathtt{Vari\^ancia\quad (adu)}$', size=font)
	plt.ylabel(r'$\mathtt{Intensidade \quad do \quad sianl \quad (e-)}$', size=font)
	plt.title(r'$\mathtt{Curva \quad da \quad intensidade \quad do \quad sinal \quad em \quad fun}$'+ u'ç'+ r'$\mathtt{\~ao \quad da\quad vari\^ancia}$'+'\n', size=font)
	plt.xlim(xmin=0.99*X[0], xmax=1.01*X[-1])
	plt.ylim(ymin=0.99*Y[0], ymax=1.01*Y[-1])
	plt.text(0.50,0.15, r'$\mathtt{Ganho: \quad %.2f^+_- %.2f}$'%(coefAng, stdLinAjust), va='center', ha='left', size=font+5,transform=ax.transAxes)	
	plt.text(0.50,0.08, r'$\mathtt{\sigma_e = \; %.2f^+_- %.2f}$'%(readNoise, stdReadNoise), va='center', ha='left', size=font+5, transform=ax.transAxes)

	return coefAng


def Graph_residuos(x,y, std):
	i,font, residuo,err = 0, 17, [], []
	for dado in y:
		residuo.append(dado - coefAng*x[i]- intercept)
		i+=1
	for dado in std:
		err.append(sqrt(dado**2+stdLinAjust**2))

	ax = plt.subplot(122)
	plt.plot(x, residuo, c='blue')
	plt.errorbar(x, residuo, err, c='blue', fmt='o')
	plt.xlabel(r'$\mathtt{Vari\^ancia \quad (adu)}$', size=font)
	plt.ylabel(r'$\mathtt{Intensidade \quad do \quad sinal \quad (e-)}$', size=font)
	plt.title(r'$\mathtt{Curva: \quad res \acute\iota duos \quad = \quad sinal \quad - \quad ajuste \quad linear}$'+'\n', size=font)
	plt.xlim(xmin=0.99*x[0], xmax=1.01*x[-1])
	linhaReferencia(x,residuo)

	num  = algarismoSig(np.std(residuo))
	mean = str(round(np.mean(residuo), num))
	std  = str(round(np.std(residuo),num))
	if  '-0.0' == mean:
		mean = mean[1:]
	plt.text(0.05,0.9, r'$\mathtt{M\acuteedia \; = \; %s^+_- \; %s \quad el\acuteetrons}$'%(mean,std), va='center', ha='left', size=font+3, transform=ax.transAxes)
	
	
	
