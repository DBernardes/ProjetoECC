#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 20 de Outubro de 2016.
    
    Descricão: este modulo tem como entrada duas lista: eixos x e y de um gráfico. A saida sera um novo grafico com a media dos bins (para um dado tamanho fornecido) em funcao de x.
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
 
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


import numpy as np
import matplotlib.pyplot as plt

from porcentPixel import porcentPixel as porcent


#biblioteca para binagem dos dados, fornecidos os vetores x e y, com um passo binsize
def binagem(x,y, binsize=50):
	i=0
	lenDados=len(y)
	vetorBinMean = []
	xbin = []
	stdBin = []
	while i < lenDados:
		binmean = np.mean(y[i:i+binsize])
		vetorBinMean.append(binmean)
		xbin.append(np.mean(x[i:i+binsize]))
		stdBin.append(np.std(np.abs(y[i:i+binsize]-binmean)))
		i+=binsize

	plt.plot(xbin,vetorBinMean,linewidth=1.5, c='blue')
	plt.errorbar(xbin, vetorBinMean, stdBin, marker='o', c='blue',linewidth=1.5)

	meanBin = np.mean(vetorBinMean)
	meanStdbin = np.mean(stdBin)
	porcentBin = porcent(vetorBinMean)
	return meanBin, meanStdbin, porcentBin
