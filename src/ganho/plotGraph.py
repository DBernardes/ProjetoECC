#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
	Descricao: este modulo tem como entrada um dicionario contendo a serie de dados (x,y), fazendo o plot dessas informacoes em um grafico, realizando um ajuste linear da curva e exibindo os coeficientes linear a angular.
    
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
from linhaReferencia import linhaReferencia
from algarismoSig import algarismoSig


def Graph_sinal_variance(X, Y, std, Estd):
	font = 17	
	global coefAng, intercept, stdLinAjust
	coefAng, intercept, r, p, stdLinAjust = stats.linregress(X,Y)
	ajust = np.poly1d((coefAng,intercept))	
	ax = plt.subplot(121)
	plt.plot(X, Y, '-', c='blue')	
	plt.errorbar(X,Y,std, fmt='o', c='blue')
	plt.plot(X, ajust(X), c='red')	
	plt.xlabel(r'$\mathtt{Vari\^ancia\quad (adu)}$', size=font)
	plt.ylabel(r'$\mathtt{Intensidade \quad do \quad sianl \quad (e-/pixel)}$', size=font)
	plt.title(r'$\mathtt{Curva \quad da \quad intensidade \quad do \quad sinal \quad em \quad fun}$'+ u'ç'+ r'$\mathtt{\~ao \quad da\quad vari\^ancia}$'+'\n', size=font)
	plt.text(0.55,0.15, r'$\mathtt{Ganho: \quad %.2f^+_- %.2f}$'%(coefAng, stdLinAjust), va='center', ha='left', size=font+5,transform=ax.transAxes)	
	plt.text(0.55,0.08, r'$\mathtt{\sigma_e = \; %.2f^+_- %.2f}$'%(intercept, Estd), va='center', ha='left', size=font+5, transform=ax.transAxes)

	return coefAng


def Graph_residuos(x,y, std):
	i,font, residuo = 0, 17, []
	for dado in y:
		residuo.append(dado - coefAng*x[i]- intercept)
		i+=1
	ax = plt.subplot(122)
	plt.plot(x, residuo, c='blue')
	plt.errorbar(x, residuo, std, c='blue', fmt='o')
	plt.xlabel(r'$\mathtt{Vari\^ancia \quad (adu)}$', size=font)
	plt.ylabel(r'$\mathtt{Intensidade \quad do \quad sinal \quad (e-/pixel)}$', size=font)
	plt.title(r'$\mathtt{Curva: \quad res\acuteiduos \quad = \quad sinal \quad - \quad ajuste \quad linear}$'+'\n', size=font)
	plt.xlim(xmin=0.9*x[0], xmax=1.02*x[-1])
	linhaReferencia(x,residuo)

	num  = algarismoSig(np.std(residuo))
	mean = str(round(np.mean(residuo), num))
	std  = str(round(np.std(residuo),num))
	plt.text(0.05,0.9, r'$\mathtt{M\acuteedia \; = \; %s^+_- \; %s \quad (adu)}$'%(mean,std), va='center', ha='left', size=font+3, transform=ax.transAxes)
	
	
	
