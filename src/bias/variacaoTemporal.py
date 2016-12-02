#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 17 de Agosto 2016.
    
    Descricao: este modulo possui como input uma serie de dados obtidos pelo CCDs, retornando o valor da mediana dos pixels de cada imagem em funcao do tempo, assim como o desvio padrao absoluto. Alem disso, e calculada a transformada de Fourier para essa serie, permitindo uma comparacao entre os dois tipos de graficos.
    
    @author: Denis Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import numpy as np
import matplotlib.pyplot as plt
import ecc_utils as ecc
import astropy.io.fits as fits

from scipy.fftpack import fft, fftfreq
from detect_peaks import detect_peaks
from probPico import probPico
from sinalReferencia import sinalReferencia
from caixaTexto import caixaTexto as caixa
from algarismoSig import algarismoSig
from divideLista import calcIteracao




def geraDados(imagefiles):
	#separada a lista total e fragmentos menores 
	listaSeparada = calcIteracao(imagefiles)
	vetorMean,vetorStddev,vetorMedAbsdev=[],[],[]

	for lista in listaSeparada:		
		dados = []
		for img in lista:
			dados.append(fits.getdata(img, 0)[0])	
		for img in dados:	
			#Dados		
			meanvalue = np.mean(img)	
			#Media e desvio padrao
			vetorMean.append(meanvalue)
			vetorStddev.append(np.std(img))	
			# Desvio padrao absoluto
			devscidata = np.abs(img - meanvalue)	
			vetorMedAbsdev.append(np.std(devscidata))
		#FFT	
		Meanf = np.abs(fft(vetorMean))
		interv = len(Meanf)/2	
		Meanf = Meanf[1:interv]
		xf = fftfreq(len(vetorMean))
		xf = xf[1:interv]
			
	
		#Linha referencia	
		meanTotal = range(len(vetorMean))
		y = np.mean(vetorMean)
		for i in meanTotal:
			meanTotal[i] = y
	
	return vetorMean, vetorStddev, Meanf, xf, meanTotal, interv




#Grafico da media pelo tempo
def plotGraficoTemporal(x,y,stddev,meanTotal):
	passo = len(x)/50
	font=20
	ax1= plt.subplot2grid((4,3),(2,0),colspan=2)
	plt.xlabel(r'$\mathtt{Tempo (s)}$', size=font)
	plt.ylabel(r'$\mathtt{Contagens \; (adu)}$',size=font)
	plt.title(r'$\mathtt{Media \quad das \quad imagens \quad em \quad fun}$' + u'ç' + r'$\mathtt{\~ao \quad do \quad tempo}$',size=font+2)
	plt.scatter(x,y, label=r'$\mathtt{Media \; temporal}$',marker='.',color='blue',alpha=0.8)
	plt.xlim(xmin = x[0], xmax = x[-1])
	#linha de referencia
	plt.plot(x,meanTotal, color='red', label=r'$\mathtt{Media \; total}$',linewidth=2)
	plt.legend(loc='upper left')


# plota grafico da FFT
def plotGraficoFFT(x,y,vetorDados,interv):	
	font=20
	sinalf, xs = sinalReferencia(vetorDados, interv)		
	meanSinal = np.mean(sinalf)
	stdSinal = np.std(sinalf)
	meanDados = np.mean(y)
	stdDados = np.std(y)


	picos = detect_peaks(y,threshold = meanSinal+3*stdSinal)
	npicos = range(len(picos))
	if len(picos) == 0:
		npicos = 0
		
	
	ax2 = plt.subplot2grid((4,3),(3,0),colspan=2)
	plt.plot(x,y, label = r'$\mathtt{fft \; dos \; Dados}$ ',marker='o',c='blue')
	plt.plot(x,sinalf, label = r'$\mathtt{sinal \; de \; refer\^encia}$', color='red',alpha=0.9)
	plt.title(r'$\mathtt{Transformada \quad de \quad Fourier}$',size=font)
	plt.xlabel(r'$\mathtt{Frequ\^encia \; (Hz)}$',size=font)
	plt.ylabel(r'$\mathtt{Amplitude}$',size=font)	
	plt.legend(loc='lower right')

	if npicos != 0:
		for i in npicos:
			plt.annotate(r'$\mathtt{%i}$' %(i+1), xy=(0.95*x[picos[i]],y[picos[i]]), xycoords='data',fontsize=17)

	return npicos, picos



#Dados para a caixa de texto da FFT
def dadosFFT(vetory, vetorx, npicos, picos):
	vetorProb = probPico(vetory, picos)

	ax3 = plt.subplot2grid((4,3),(3,2))
	plt.xticks(())
	plt.yticks(())
	plt.title(r'$\mathtt{pico \;  (n): \;  (frequ\^encia, \;  amplitude, \;  chance \;\;  de \;\;  erro \; )}$', size=17)
	if npicos != 0:	
		for i in npicos:
			if i < 8:		
				textstr = r'$\mathtt{pico \; %i: \;(%.3f \;\; Hz,%.2f \;\;adu, \; %.3f \;}$' %(1+i,vetorx[picos[i]-1],vetory[picos[i]-1], vetorProb[i]*100)  +'%' + r'$\mathtt{)}$'
				plt.text(0.03, 0.94-0.1*i, textstr, ha='left', va='center', size=20)
			else:
				plt.text(0.03, 0.92-0.1*i, r'$\mathtt{Quantidade \;\; de \;\; picos}$'+'\n'+ r'$\mathtt{ \;\; muito \;\; alta.}$', ha='left', va='center', size=21)
				break
	else:		
		plt.text(0.03, 0.90, r'$\mathtt{Nenhum \;\; pico \;\; encontrado.}$', ha='left', va='center', size=21)




#Caixa de texto com dados da media temporal
def dadosMeanTemp(vetor,vetorstd):	
	mean = np.mean(vetor)
	std = np.std(vetor)
	meanStd = np.mean(vetorstd)
	ratio = meanStd/std

	num = algarismoSig(std)
	mean = str(round(mean,num))
	std = str(round(std,num))	

	meanFrame = vetor[0]
	stdFrame  = vetorstd[0]
	num = algarismoSig(stdFrame)
	meanFrame = str(round(meanFrame,num))
	stdFrame = str(round(stdFrame,num))	

	
	sinal=None
	textstr0 = ''
	textstr1 = r'$\mathtt{\barM_{temp} = \; %s_-^+ \; %s \;\; adu}$' %(mean,std)
	textstr2 = r'$\mathtt{\barM_{frame} = \; %s_-^+ \; %s \;\; adu}$' %(meanFrame,stdFrame)
	textstr3 = r'$\mathtt{\bar\sigma_{frame} = \; %.1f \; \sigma_{temp}}$' %(ratio)
	if ratio > 1.1:
		sinal =  r'$\mathtt{\gg}$'
	if  0.9 < ratio < 1.1:
		sinal =  r'$\mathtt{\approx}$'
	if ratio < 0.9:	
		sinal =  r'$\mathtt{\ll}$'

	textstr4 =   r'$\mathtt{\bar\sigma_{frame}}$' + sinal + r'$\mathtt{ \sigma_{temp} \;\; (>10}$' + '%'+ r'$\mathtt{)}$'

	textstr = [textstr0,textstr1,textstr2,textstr3,textstr4]
	caixa(textstr, 4, 3, 2, 2, font=26, space=0.15)

#--------------------------------------------------------------------------------------------


def variacaoTemporal(inputlist, tempoExp):
	
	vetorMean, vetorStddev, Meanf, xf, meanTotal,interv = geraDados(inputlist)	
	x = np.linspace(0,tempoExp,len(inputlist))		

	#Grafico media das imagens pelo tempo
	plotGraficoTemporal(x,vetorMean,vetorStddev,meanTotal)	
	#Caixa de texto com dados da media temporal
	dadosMeanTemp(vetorMean,vetorStddev)	
	#Grafico da FFT
	npicos, picos = plotGraficoFFT(xf,Meanf,vetorMean,interv)
	#Caixa de texto da FFT	
	dadosFFT(Meanf[1:interv],xf[1:interv], npicos, picos)

	
	 

  
