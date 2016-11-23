#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 17 de Agosto de 2016.
    
    Descricao: este modulo gera um histograma dos dados fornecido pelo script geraArquivo.py. Sore esses dados e calculado a media, mediana, desvio padrao e desvio padrao absoluto. Alem disso, e gerado um segundo histograma normalizado emrelacao a media e desvio padrao obtidos. Um intervalo de 2sigma e estipulado ao redor da mediana, assim como cada um desses pontos sobre a curva.
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    

    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


import numpy as np
import matplotlib.pyplot as plt
import ecc_utils as ecc
import matplotlib.mlab as mlab

from scipy.interpolate import interp1d
from algarismoSig import algarismoSig

#gera os dados principais do histograma
def geraDados(image):	
	mean = np.mean(image)
	median = np.median(image)
	std = np.std(image)
	stdAbs = np.std(np.abs(image - median))

	value,base = np.histogram(image, bins= np.linspace((median-7*stdAbs),(median+7*stdAbs),18), normed=1)
	x = np.linspace(base[0],base[-1],100)
	y = mlab.normpdf(x, mean, std)

	i=0
	while i<len(value):
		value[i]*=100
		i+=1

	i=0
	while i<len(y):
		y[i]*=100
		i+=1
	
	return mean, median, std, stdAbs, value, base, x, y


# plota grafico do histograma
def plothist(base, value, x, y, mean, median, std, stdAbs):
	ax= plt.subplot2grid((4,3),(1,1),colspan=1)
	font=20
	plt.plot(base[:-1],value,c='blue')
	plt.plot(x,y,'--',c='red')
	plt.xlabel(r'$\mathtt{Contagens \; (adu)}$',size=font)
	plt.ylabel(r'$\mathtt{Frequ\^encia\;}$'+'(%)',size=font)
	plt.title(r'$\mathtt{Histograma \quad da \quad imagem \quad combinada}$',size=font)

	
	f = interp1d(base[:-1], value, kind='cubic')	
	x16 = mean-std
	x50 = mean
	x84 = mean+std	

	index16 = returnIndex(x,x16)
	index84 = returnIndex(x,x84)
	plt.ylim(ymax=1.1*f(x50))
	plt.plot(median, f(median),'o')
	drawLine(x16,0,f(x16),'1', pos='left')
	drawLine(x84,0,f(x84),'3')	
	plt.annotate('2',xy=(median*1.0001,f(median)*1.001),xycoords='data',size=17)
	plt.annotate('',xy=(x16,f(x16)/2), xycoords='data',xytext=(x84,f(x16)/2), textcoords='data',arrowprops=dict(arrowstyle="<->"),)
	plt.annotate(r'$\mathtt{\sigma^+_-}$', xy=(x50*0.9999,1.08*f(x16)/2), xycoords='data',fontsize=14)

	# Informacões dos intervalor da media +/- sigma

	num = algarismoSig(std)
	mean = str(round(mean,num))
	std = str(round(std,num))

	num = algarismoSig(stdAbs)
	median = str(round(median,num))
	stdAbs = str(round(stdAbs,num))

	textstr0 = ''
	textstr1 = ''
	textstr2 =  r'$\mathtt{Histograma: }$'
	textstr3 =  r'$\mathtt{Media= \; %s_-^+ \; %s \quad adu}$' %(mean, std)
	textstr4 =	r'$\mathtt{Mediana= \; %s_-^+ \; %s \quad adu}$'%(median,stdAbs)                                                                                                              
	textstr5 =  r'$\mathtt{1 \; - \;(%.2f \; adu,%.2f}$'%(x16,f(x16)) +' %' + r'$\mathtt{)}$'
	textstr6 =  r'$\mathtt{2 \; - \;(%.2f \; adu,%.2f}$'%(x50,f(x50)) +' %' + r'$\mathtt{)}$'
	textstr7 =  r'$\mathtt{3 \; - \;(%.2f \; adu,%.2f}$'%(x84,f(x84)) +' %' + r'$\mathtt{)}$'

	textstr = [textstr0,textstr1,textstr2,textstr3,textstr4,textstr5, textstr6, textstr7]	
	return textstr


# retorna o indice dado um vetor e um parametro
def returnIndex(vetor,parameter):
		i=0
		for valor in vetor:
			if round(valor/parameter,3) == 1.0:
				return i
				break
			i+=1 


# desenha uma linha com as coordenadas especificadas
def drawLine(x1,y1,y2,text,font=17,pos='right'):	
	plt.annotate('',xy=(x1,y1), xycoords='data',xytext=(x1,y2), textcoords='data',arrowprops=dict(arrowstyle="-"),)
	textstr = text
	if pos == 'right':
		plt.text(x1*1.00005,y2, textstr, ha='left', va='center', size=font)
	if pos == 'left':
		plt.text(x1*0.9995,y2, textstr, ha='left', va='center', size=font)
	plt.plot(x1,y2,'o',color='blue')	

#--------------------------------------------------------------------------------------------------

def histograma(image):

	mean, median, std, stdAbs, value, base, x, y = geraDados(image)
	textstr = plothist(base, value, x, y, mean, median, std, stdAbs)									
	return textstr, mean

		