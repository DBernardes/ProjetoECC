#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
	Descricao: este modulo tem como entrada um dicionario contendo a serie de dados de sinal x variancia, fazendo o plot dessas informacoes em um grafico, realizando um ajuste linear da curva e exibindo a respectiva equacao.
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import matplotlib.pyplot as plt
import numpy as np

def plotGraph(X, Y, std):
	font = 17	
	coefAjust = np.polyfit(X, Y,1)
	ajust = np.poly1d(coefAjust)	
	ax = plt.subplot(111)
	plt.plot(X, Y, '-', c='blue')	
	plt.errorbar(X,Y,std, fmt='o', c='blue')
	plt.plot(X, ajust(X), c='red')	
	plt.xlabel(r'$\mathtt{Contagens\quad (adu)}$', size=font)
	plt.ylabel(r'$\mathtt{e-/pixel}$', size=font)
	plt.title(r'$\mathtt{Curva \quad da \quad intensidade \quad do \quad sinal \quad em \quad fun}$'+ u'ç'+ r'$\mathtt{\~ao \quad das\quad contagens}$'+'\n', size=font)
	plt.text(0.70,0.15, r'$\mathtt{Ganho: \quad %.2f}$'%(coefAjust[0]), va='center', ha='left', size=font,transform=ax.transAxes)	
	plt.text(0.70,0.10, r'$\mathtt{\sigma_e = \; %.2f}$'%(coefAjust[1]), va='center', ha='left', size=font, transform=ax.transAxes)

	return coefAjust[0]
