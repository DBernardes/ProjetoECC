#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    Laboratorio Nacional de Astrofisica, Brazil.
    @author: Denis Varise Bernardes & Eder Martioli
    Descricao: esta bibloteca possui as seguintes funcoes:
	
		GeraVetorFluxoCamera: esta funcao tem como entrada o header de uma imagem, o numero de imagens com o mesmo comprimento de
		onda e o ganho do CCD previamente medido; sua tarefa e fornecer a imagem, tempo de exposicao, o valor da mediana do background
		e valor do ganho de cada imagem para a funcao calcFluxo, que retornara o valor do fluxo do CCD, adicionando-o a um vetor.    

		criaArqFluxoCamera: fornecido os vetores do fluxo da camera e desvio padrao do fluxo, esta funcao cria o arquivo Fluxocamera.dat,
		escrevendo o conteudo destes dois vetores em duas colunas.

   		calcFluxo: dado os parametros: imagem, tempo de exposicao, medianBackground, stdBackground e ganho, esta funcao calculara o
   		valor do fluxo de fotons para a regiao dentro de uma caixa de pixels. Para tanto, faz a chamada da funcao caixaPixels.

		caixaPixels: fornecida a imagen e os valores das coordenadas centrais de dimensao da caixa, retorna um array dos pixels internos
		a essa regiao.

		getVetorEtime: dado o numero de imagens com mesmo adquiridas para o mesmo comprimento de onda, retorna o valor do tempo de
		exposicao da lista de imagens.

		getDadosBackground: esta funcao faz a leitura dos dados do arquivo dadosBackground.dat gerado anteriormente, retornando dois
		vetores: mediana e desvio padrao do background.

		CalcErroDetector: esta funcao tem como proposito calcular a porcentagem do erro do detector para um dado comprimento de onda.
		O funcionamento desta funcao foi baseada na descricao do manual de operaçao do dispositivo (OL-750-HSD-301C,  Optronic Laboratories, Inc.).

		FluxoRelativo: esta funcao faz o calculo do fluxo relativo entre o CCD e o detector; junto a isso, faz a correcao do valor obtido
		para a curva de calibracao do detector (realiza a leitura do arquivo da curva de calibracao do detector fornecido pela chamada da
		funcao LeArq_curvaCalibDetector). Faz a somatoria da variancia das imagens com a variancia do detector (obtido pela chamada da
		funcao CalcErroDetector), convertendo adicionando seu valor a um vetor.

	example: ./BackgroundCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import astropy.io.fits as fits
import numpy as np
import os

from math import sqrt, cos
from scipy.interpolate import interp1d
from QE_reduceImgs_readArq import LeArquivoReturnLista, LeArq_curvaCalibFiltroDensidade
from QE_GraphLib import returnMax

import matplotlib.pyplot as plt


def GeraVetorFluxoCamera(header,ganho, tagDado, tagRef, lenPixel, Dfotometro, images_path):        
	print('\nCalculando o fluxo total da camera \n')
	chdir = images_path + '\\' + 'Imagens_reduzidas'
	coordx	   = int(header['naxis1']/2)
	coordy 	   = int(header['naxis2']/2)
	Cdimension = int(Dfotometro/(lenPixel*1e-3)) #dimensao do fotometro dividido pelo tamanho do pixel do CCD = numero de pixels necessarios para a dimensao da caixa de pixels. 
	
	etime2 = getVetorEtime(tagDado, images_path)
	etime1 = getVetorEtime(tagRef, images_path)
	VetorStdDiff = getStdDiffImages(images_path)
	
	vetorFluxoCamera, i = [], 0
	with open(chdir + '\\' + 'listaImagensReduzidas') as f:
		lista = f.read().splitlines()
		for img in lista:
			data = fits.getdata(chdir + '\\' + img)
			data = caixaPixels(data,(coordx,coordy,Cdimension))	
			fluxo = calcFluxo(data, etime2[i]-etime1[i], ganho)
			vetorFluxoCamera.append(fluxo)						
			i+=1						
		f.close()		
	criaArqFluxoCamera(vetorFluxoCamera, VetorStdDiff, images_path)	



def caixaPixels(imagem, tupla):
	#retira apenas uma caixa de pixels, dada as coordenadas (x,y) e seu tamanho			
	xcoord = tupla[0]
	ycoord = tupla[1]
	dimension = int(tupla[2]/2)
	d = dimension
	imagem = imagem[xcoord-d:xcoord+d,ycoord-d:ycoord+d]
	return imagem



def calcFluxo(data, etime, ganho):
	Somapixels = sum(sum(data))*ganho #soma dos valores dos pixels subt. do Background mediano
	fluxoImagem = Somapixels/etime #contagens totais pelo tempo de exposicao	
	
	return fluxoImagem



def FluxoRelativo(Fluxocamera,Fluxodetector, Stdcamera, Strespectro, nomeArq_CalibFiltroDensidade, images_path):	
	vetorEQ, vetorSigmaTotal = [], []
	Split_Str_espectro = Strespectro.split(',')
	Einicial = int(Split_Str_espectro[0])
	Efinal   = int(Split_Str_espectro[1])
	step     = int(Split_Str_espectro[2])
	n = int((Efinal - Einicial)/step) + 1
	espectro = np.linspace(Einicial, Efinal, n)
	
	

	VetorFiltroDensidade = LeArq_curvaCalibFiltroDensidade(nomeArq_CalibFiltroDensidade, n, images_path)
	for i in range(len(Fluxocamera)):
		h = 6.62607004e-34 
		c = 299792458 #m/s		
		ErroPorcentDetector = CalcErroDetector(espectro[i])	
		
		#caso nao seja fornecido o nome do arquivo do filtro de densidade, a funcao retornara um vetor contendo apenas o valor 1.
		A = Fluxocamera[i]*100
		B = VetorFiltroDensidade[i]*Fluxodetector[i]*espectro[i]*1e-9/(h*c)		
		sigmaDetector = ErroPorcentDetector*B
		EQ = A/B
		#print(A/(VetorFiltroDensidade[i]*espectro[i]*1e-9/(h*c))/0.27)
		varianceTotal = EQ**2*((Stdcamera[i]/A)**2+(sigmaDetector/B)**2)
		vetorEQ.append(EQ)
		vetorSigmaTotal.append(sqrt(varianceTotal))
		i+=1
	return vetorEQ, vetorSigmaTotal




def getVetorEtime(tagDado, images_path):
	arquivoListaImagens = tagDado+'List.txt'
	vetorEtime = []
	listaImagens = LeArquivoReturnLista(arquivoListaImagens, images_path)
	for i in range(len(listaImagens)):
		header = fits.getheader(listaImagens[i])
		vetorEtime.append(header['exposure'])
	return vetorEtime

		


def getStdDiffImages(images_path):
	StdDiff = []
	with open(images_path + '\\' + 'StdDiffImages') as arq:
		listaValues = arq.read().splitlines()
		for linha in listaValues[1:]:			
			StdDiff.append(float(linha))			
		arq.close()
	return StdDiff




def CalcErroDetector(Comp_onda):
	photodiodeError = 0
	NIST_OLSD = 0.005
	if 250< Comp_onda < 400:
		photodiodeError = 0.010	
	if 400< Comp_onda < 900:
		photodiodeError = 0.005
	if 900< Comp_onda < 1000:
		photodiodeError = 0.022
	if 1000< Comp_onda < 1100:
		photodiodeError = 0.022	
	
	ErroDetector = NIST_OLSD**2 + photodiodeError**2 

	return sqrt(ErroDetector)




def criaArqFluxoCamera(VetorF, vetorSigma, images_path):
	nome = images_path + '\\' + 'Fluxo camera.dat'
	try: 
		arq = open(nome, 'w')
	except:
		nome.remove()
		arq = open(nome, 'w')
	arq.write(' Fluxo (e/s)			Sigma (e/s)\n')
	for i in range(len(VetorF)):
		arq.write('%e \t\t\t %f\n' %(VetorF[i], vetorSigma[i]))
	arq.close()


