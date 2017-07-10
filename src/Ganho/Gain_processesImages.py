#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
    Descricao: esta biblioteca possui as seguintes funcoes:
		parametrosCaixaPixels: esta funcao recebe o nome de uma unica imagens, retornando os valores da coordenada central e dimensao da caixa de pixels.

		organizaCombinacoes: esta funcao recebe uma lista de imagens e retorna um vetor com as possiveis combinacoes de pares entre elas.

		recebeListaImgs_geraArqListaCombinacoes: esta funcao recebe uma lista de imagens flat e o numero de imagens adquiridas para a mesma intensidade de luz. Para cada conjunto de n imagens, adiciona a um vetor as possiveis combinacoes entre pares detes conjunto atraves da funcao organizaCombinacoes; ao terminar os conjuntos, a funcao escreve em um arquivo chamado arquivoListaCombinacoes os pares de imagens separados em colunas.

		LeArqImgsFlat_retornaListaImgs: esta funcao faz a leitura do arquivo arquivoListaCombinacoes criado pela funcao recebeListaImgs_geraArqListaCombinacoes, retornando uma lista com o nome dessas imagens.

		calcXY_YerrorBar_XerrorBar: esta funcao recebe uma lista de imagens flat, uma lista de imagens bias e o numero de imagens adquiridas para cada patamar de intensidade de luz. Ela realiza o calculo da intensidade do sinal (em eletrons) e do valor da variancia comparando duas imagens de bias e duas imagens de flat. Para isso, faz a chamada da funcao recebeListaImgs_geraArqListaCombinacoes que tomara as imagens obtidas e, dado o numero de imagens em cada conjunto, retorna uma lista de duas colunas com cada par de combinações possíveis. Para cada par de imagens é retirada uma caixa de pixels de 100 x 100 no centro da imagem; sobre essa caixa será calculada a intensidade do sinal (EixoY), a variancia (EixoX), o desvio padrao das medidas (StdEixoY) e a barra de erro para os valores em X.

    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import astropy.io.fits as fits
import numpy as np
from math import sqrt, factorial



def parametrosCaixaPixels(parametros, imagem, box=100):
	if parametros == '':
		header = fits.getheader(imagem)
		coordx	   = header['naxis1']/2
		coordy 	   = header['naxis2']/2
		b = box/2
	else:
		parametros = parametros.split(',')
		coordx = int(parametros[0])
		coordy = int(parametros[1])
		b = int(parametros[2])/2
	return [coordx, coordy, b]


def organizaCombinacoes(lista, newlist=[[],[]]):	
	for imgA in lista:
		for imgB in lista:
			if imgA != imgB:				
				newlist[0].append(imgA)
				newlist[1].append(imgB)
		lista.remove(imgA)
		organizaCombinacoes(lista, newlist)
		return newlist


def recebeListaImgs_geraArqListaCombinacoes(listaFlat, numeroImagens):
	for z in range(len(listaFlat))[::numeroImagens]:
		listaConjuntos = listaFlat[z:z+numeroImagens]
	 	listaCombinacoes = organizaCombinacoes(listaConjuntos)		

	name = 'arquivoListaCombinacoes'
	try:arq = open(name, 'w')
	except: 
		name.remove()
		arq = open(name,'w')
	for i in range(len(listaCombinacoes[0])):
		s = listaCombinacoes[0][i] + ' ' + listaCombinacoes[1][i] + '\n'
		i+=1
		arq.write(s)
	arq.close()


def LeArqImgsFlat_retornaListaImgs():
	listaImgs = []
	with open('arquivoListaCombinacoes') as arq:
		Listalinhas = arq.read().splitlines()
		for linha in Listalinhas:
			for img in linha.split(' '):		
				listaImgs.append(img)
	arq.close()	
	return listaImgs



#----------------------------------------------------------------------------------------------------------------------------------
def calcXY_YerrorBar_XerrorBar(listaFlat, listaBias, numeroImagens, parametersBox):	
	coordx = parametersBox[0]
	coordy = parametersBox[1]
	b = parametersBox[2]
	X, Y, SigmaTotal = [], [], []
	VetorEixoX, VetorEixoY,VetorStdEixoY, VetorStdEixoX,XsigmaBar = [], [], [], [], []
	lenListaBias = len(listaBias)

	recebeListaImgs_geraArqListaCombinacoes(listaFlat, numeroImagens)	
	nCombinacoes = factorial(numeroImagens)/(factorial(2)*factorial(numeroImagens-2))
	listaImgs = LeArqImgsFlat_retornaListaImgs()

	#le imagens de flat
	for i in range(len(listaImgs))[::2]:
		FlatA = fits.getdata(listaImgs[i])  [0]
		FlatB = fits.getdata(listaImgs[i+1])[0]
		BiasA = fits.getdata(listaBias[(i/2)%lenListaBias])    [0]
		BiasB = fits.getdata(listaBias[((i+2)/2)%lenListaBias])[0]	
				
		FlatA = FlatA[coordx-b:coordx+b,coordy-b:coordy+b].astype(float)
		FlatB = FlatB[coordx-b:coordx+b,coordy-b:coordy+b].astype(float)
		BiasA = BiasA[coordx-b:coordx+b,coordy-b:coordy+b].astype(float)
		BiasB = BiasB[coordx-b:coordx+b,coordy-b:coordy+b].astype(float)

		sigmaBias = np.std(BiasA - BiasB)
		sigmaFlat = np.std(FlatA - FlatB)
		Eixoy = (np.median(FlatA)+np.median(FlatB)-np.median(BiasA)-np.median(BiasB))/(sqrt(2)*sigmaBias)
		Eixox = sigmaFlat**2/(sigmaBias*sqrt(2))
		StdEixoY = sqrt(np.std(FlatA)**2 + np.std(FlatB)**2 + np.std(BiasA)**2 + np.std(BiasB)**2)/(sqrt(2)*sigmaBias)

		VetorEixoX.append(Eixox)
		VetorEixoY.append(Eixoy)
		VetorStdEixoY.append(StdEixoY)	
		
		if (i/2)%nCombinacoes == nCombinacoes-1:				
			Y.append(np.mean(VetorEixoY))
			X.append(np.mean(VetorEixoX))
			SigmaTotal.append(np.mean(VetorStdEixoY))		
			XsigmaBar.append(np.std(VetorEixoX))			
			VetorEixoX, VetorEixoY, VetorStdEixoY, VetorEixoX = [], [], [], []	
	
	return X,Y,SigmaTotal, XsigmaBar, sigmaBias
	

