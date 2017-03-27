#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 4 de Outubro de 2016  
    Descricao: esta bilbioteca possui as seguintes funcoes:

		calcDerivada_XY: esta funcao recebe uma serie de imagens e respectivos tempo de exposicao. Sobre essa serie e calculado um ajuste linear para a media dos pixels ao longo das colunas e ao longo das linhas em funcao do tempo de exposicao, sendo a derivada desta curva o valor da corrente de escuro. 

		plotGrafico: esta funcao plota um grafico para os valores x e y fornecidos. Sobre essa serie de dados e tracada uma linha de referencia para media +/- desvio padrao e calculada uma binagem dos dados para cada intervalo de 50 pontos.

		caixaTexto: esta funcao recebe os principais valores obtidos no plot dos grafico, expressando-os numa caixa de texto lateral.

		DCderivada: esta funcao recebe uma lista de imagens de dark e o header de uma das imagens, retirando e fornecendo as informacoes necessarias para todas as outras funcoes.

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
import astropy.io.fits as fits

from binagem import binagem as bins
from caixaTexto import caixaTexto as caixa
from linhaReferencia import linhaReferencia 
from algarismoSig import algarismoSig
from DC_readArq import readArq_Etime


#gera os dados principais para plotagem dos graficos
def calcDerivada_XY(dados, etime, gain, lenLinha, lenColuna):	
	xlinha = range(lenLinha)
	xcoluna = range(lenColuna)
	derivy = []
	derivx = []	
	i=0
	while i < lenLinha:
		vetorlinha = []
		for img in dados:
			vetorlinha.append(np.mean(img[i])*gain)
		coefAjust = np.polyfit(etime,vetorlinha,1)
		derivy.append(coefAjust[0])
		i+=1	
	
	j=0
	while j < lenColuna:
		meanColuna = []
		for img in dados:
			i=0
			vetorcoluna = []
			while i < lenLinha:
				vetorcoluna.append(img[i][j])
				i+=1			
			meanColuna.append(np.mean(vetorcoluna)*gain)					
		coefAjust = np.polyfit(etime,meanColuna,1)
		derivx.append(coefAjust[0])
		j+=1	

	return derivx, derivy, xlinha, xcoluna




#plota o grafico assim como suas linhas de referencia
def plotGrafico(x,y,posx, posy, temperatura, eixo='x'):	
	font = 20
	mean = np.mean(y)
	std = np.std(y)
	ax = plt.subplot2grid((3,2),(posx,posy))
	plt.scatter(x,y, marker='.', c='gray', alpha=0.5)	
	plt.xlim(xmin = x[0], xmax = x[-1])	
	plt.ylabel(r'$\mathtt{DC \quad (e-/pix/s)}$', size=font-1)
	if eixo  == 'x':
		plt.xlabel(r'$\mathtt{Eixo \;\; x}$', size=font)
		plt.title(r'$\mathtt{Gradiente\quad da \quad corrente \quad de \quad escuro}$', size=font)
	else:
		plt.xlabel(r'$\mathtt{Eixo \;\; y}$', size=font)

	plt.annotate(r'$\mathtt{Temperatura: \; %i^oC}$'%(temperatura), xy=(0.50,0.90), ha='left', va='center', size=font-2, xycoords='axes fraction')
	
	linhaReferencia(x,y) 
	meanBin, meanStdbin = bins(x,y)

	return mean, std, meanBin, meanStdbin
	

def caixaTexto(mean, std, meanBin, meanStdbin, posx, posy):
	ratio = std/meanStdbin
	sinal = None

	num = algarismoSig(std)
	mean = str(round(mean,num))
	std = str(round(std,num))

	num = algarismoSig(meanStdbin)
	meanBin = str(round(meanBin,num))
	meanStdbin = str(round(meanStdbin,num))

	textstr1 = r'$\mathtt{\barM = \; %s_-^+ \; %s \;\; e-/pix/s}$' %(mean,std)
	textstr2 = r'$\mathtt{\barM_{bin} = \; %s_-^+ \; %s \;\; e-/pix/s}$' %(meanBin,meanStdbin)
	textstr3 = r'$\mathtt{\sigma = \; %.1f \; \sigma_{bin}}$' %(ratio)
	
	if 0.9 < ratio < 1.1:
		sinal = [r'$\mathtt{\approx}$', '']	
	if ratio > 1.1:
		sinal = [r'$\mathtt{\gg}$', r'$\mathtt{(> \; 10}$' +' %' + r'$\mathtt{)}$']				
	if ratio < 0.9:
		sinal = [r'$\mathtt{\ll}$', r'$\mathtt{(< \; 10}$' +' %' + r'$\mathtt{)}$']

	textstr4 = r'$\mathtt{\sigma \;}$' + sinal[0] + r'$\mathtt{\; \sigma_{bin} \; }$'+sinal[1]

	textstr = [textstr1,textstr2,textstr3,textstr4]
	caixa(textstr, 3, 2, posx, posy, font=22, space=0.15)



#---------------------------------------------------------------------------------------------


def DCderivada(listaImagens, gain):
	print '\nCalculando a distribuicao da corrente de escuro pelo CCD.\n'
	header = fits.getheader(listaImagens[0])
	VetorEtime 	= readArq_Etime()
	temperatura = header['temp']
	lenLinha 	= header['naxis1']
	lenColuna 	= header['naxis2']
	dados=[]
	for img in listaImagens:
		dados.append(fits.getdata(img)[0])
	

	derivx, derivy, xlinha, xcoluna = calcDerivada_XY(dados, VetorEtime, gain, lenLinha, lenColuna)


	mean, std, meanBin, meanStdbin = plotGrafico(xcoluna, derivx, 1, 0, temperatura)	
	caixaTexto(mean, std, meanBin, meanStdbin, 1, 1)		

	mean, std,meanBin, meanStdbin = plotGrafico(xlinha, derivy, 2, 0, temperatura,'y')
	caixaTexto(mean, std, meanBin, meanStdbin, 2, 1)





	






