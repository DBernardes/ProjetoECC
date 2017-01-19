#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 29 de Agosto de 2016  
    Descricao: esta biblioteca possui as seguintes funcoes:
		plotCorrentTemp: esta funcao gera um grafico para os valores da mediana das contagem em funcao do tempo de exposicao fornecidos e do ajuste linear criado para os dados, identificando esse plot por uma cor e temperatura.

		plotTempDC: esta funcao gera um grafico da corrente de escuro em funcao da temperatura, apresentando em forma literal o valor de cada um dos pares de coordenadas.

		DCvariacaoTemporal: para cada um dos diretorios de imagens, esta funcao realiza a leitura dos arquivos de dados temporais (readArq_DadosTemporais) e do tempo de exposicao (readArq_Etime), plotando para cada um o grafico da mediana das imagens em funcao do tempo de exposicao atraves da funcao plotCorrentTemp; monta o vetor da corrente de escuro para cada uma das temperaturas (vetorCoefAJust), retornando-o para a proxima funcao - plotTempDC - para o plot do grafico da corrente de escuro em funcao da temperatura. 
				
		Ajustelinear: esta funcao constroi um vetor, dado o dominio da funcao, coeficiente angular e linear da curva
		
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import numpy as np
import matplotlib.pyplot as plt

from scipy import stats
from algarismoSig import algarismoSig
from DC_readArq import readArq_DadosTemporais, readArq_Etime



#plota grafico da DC pelo tempo
def plotCorrentTemp(x, y, std, yajust, temperatura, color):
	font = 15
	sinal=None
	plt.plot(x,y,'o', color=color,label = r'$\mathtt{Temp: \quad %i^oC}$'%(temperatura))
	plt.errorbar(x,y,std, c= color, fmt='o')	
	plt.plot(x,yajust,'-',c= color)
	plt.xlabel(r'$\mathtt{Tempo \quad de \quad exposi}$'+u'ç'+ r'$\mathtt{\~ao \; (s)}$', fontsize = font)
	plt.ylabel(r'$\mathtt{Contagens \quad (adu/pix)}$',fontsize = font)
	plt.title(r'$\mathtt{Mediana \quad das \quad contagens \quad em \quad fun}$'+u'ç'+ r'$\mathtt{\~ao \quad do \quad tempo \quad de \quad exposi}$'+u'ç'+ r'$\mathtt{\~ao}$'+'\n',fontsize = font)
	plt.legend(loc = 'upper left')
	plt.xlim(xmax = x[-1])
	plt.ylim(ymin = -5)
	



def plotTempDC(temperatura, DC, std):
	ax = plt.subplot2grid((3,2),(0,1))
	font = 15	
	i=0
	#arredonda para a casa decimal com o primeiro algarismo significativo
	while i < len(DC):
		num = algarismoSig(std[i])
		DC[i]  = round(DC[i], num)
		std[i] = round(std[i],num)
		i+=1

	plt.plot(temperatura, DC, marker='o', c='blue')
	plt.errorbar(temperatura, DC, std, c='blue', fmt='o')
	plt.xlabel(r'$\mathtt{Temperatura \quad (^oC)}$', size=font)
	plt.ylabel(r'$\mathtt{Corrente \quad de \quad escuro \quad (e-/pix/s)}$', size=font)
	plt.title(r'$\mathtt{Corrente \quad de \quad escuro \quad em \quad fun}$'+u'ç'+r'$\mathtt{\~ao \quad da \quad temperatura}$', size=font+2)
	plt.xlim(xmax=temperatura[0]*0.9)
	
	i=0
	while i < len(DC):
		DC[i]  = str(DC[i])
		std[i] = str(std[i])
		textstr = r'$\mathtt{DC(%i^oC) \; = \quad %s^+_- \; %s \; e-/pix/s}$'%(temperatura[i], DC[i], std[i])
		plt.text(0.05, 0.90-i*0.07,textstr,ha='left',va='center',size= font+1,transform=ax.transAxes)		
		i+=1
	return DC[-1]



def Ajustelinear(vetorx, Acoef, Lcoef):
	f = []
	for x in vetorx:
		f.append(Acoef*x+Lcoef)
	return f 
	

	

#-------------------------------------------------------------------------------------------------

def DCvariacaoTemporal(cwd, directories, vetorTemperatura):
	colors = ['cyan','red', 'blue','green','magenta','yellow']
	vetorCoefAJust, vetorStdLinAjust = [], []
	ax = plt.subplot2grid((3,2),(0,0))
	i=0
	for Dir  in directories:
		chdir = cwd + '/' + Dir
		os.chdir(chdir)
		VetorImgMedian, VetorStdImg, coefAjust, intercept, stdLinAjust = readArq_DadosTemporais()
		VetorEtime = readArq_Etime()
		vetorCoefAJust.append(coefAjust)
		vetorStdLinAjust.append(stdLinAjust)
		lenTemp = len(vetorTemperatura)		
		ajust = Ajustelinear(VetorEtime, coefAjust, intercept)
		plotCorrentTemp(VetorEtime,VetorImgMedian, VetorStdImg, ajust, vetorTemperatura[i], colors[i]) 	
		i+=1
	
	DCnominal = plotTempDC(vetorTemperatura, vetorCoefAJust, vetorStdLinAjust)	

	return DCnominal





