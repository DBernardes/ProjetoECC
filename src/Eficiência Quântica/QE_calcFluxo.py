#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
    Descricao: esta bibloteca possui as seguintes funcoes:
	
		GeraVetorFluxoCamera: esta funcao tem como entrada o header de uma imagem, o numero de imagens com o mesmo comprimento de onda e o ganho do CCD previamente medido; sua tarefa e fornecer a imagem, tempo de exposicao, o valor da mediana do background e valor do ganho de cada imagem para uma funcao chamada calcFluxo, que retornara o valor do fluxo do CCD, adicionando-o em seguida a um vetor.
    Laboratorio Nacional de Astrofisica, Brazil.

		criaArqFluxoCamera: fornecido os vetores do fluxo da camera e desvio padrao do fluxo, esta funcao cria o arquivo Fluxo camera.dat, escrevendo o conteudo destes dois vetores em duas colunas.

   		calcFluxo: dado os parametros imagem, tempo de exposicao, medianBackground, stdBackground e ganho, esta funcao calculara o valor do fluxo de fotons para a regiao dentro de uma caixa de pixels. Para tanto, faz a chamada da funcao caixaPixels.

		caixaPixels: fornecida a imagen e os valores das coordenadas centrais de dimensao da caixa, retorna um array dos pixels internos a essa regiao.

		getVetorEtime: dado o numero de imagens com mesmo adquiridas para o mesmo comprimento de onda, retorna o valor do tempo de exposicao da lista de imagens.

		getDadosBackground: esta funcao faz a leitura dos dados do arquivo dadosBackground.dat gera anteriormente, retornando dois vetores.

		CalcErroDetector: esta funcao tem como proposito calcular a porcentagem do erro do detector para um dado comprimento de onda. O funcionamento desta funcao foi baseada na descricao do manual de operaçao do dispositivo (OL-750-HSD-301C,  Optronic Laboratories, Inc.).

		FluxoRelativo: esta funcao faz o calculo do fluxo relativo entre o CCD e o detector; junto a isso, faz a correcao do valor obtido para a curva de calibracao do detector (realiza a leitura do arquivo da curva de calibracao do detector fornecido pela chamada da funcao LeArq_curvaCalibDetector). Faz a somatoria da variancia das imagens com a variancia do detector (obtido pela chamada da funcao CalcErroDetector), convertendo adicionando seu valor a um vetor.

	example: ./BackgroundCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import astropy.io.fits as fits
import numpy as np
import os
from math import sqrt
from QE_readImages_Arq import LeArquivoReturnLista, LeArq_curvaCalibDetector

cwd = os.getcwd()
chdir = cwd + '/' + 'Mediana das Imagens'


def GeraVetorFluxoCamera(header, nImages, ganho):
	print '\nCalculando o fluxo total da camera (W/m2)'
	coordx	   = header['naxis1']/2
	coordy 	   = header['naxis2']/2
	Cdimension = 815
	
	etime = getVetorEtime(nImages)
	dadosBackground = getDadosBackground()
	medianBackground = dadosBackground[0]
	stdBackground = dadosBackground[1]

	os.chdir(chdir)
	vetorFluxoCamera, vetorSigmaBackground_Signal, i = [], [], 0
	with open('listaImagensCombinadas') as f:
		lista = f.read().splitlines()
		for img in lista:
			print img
			data = fits.getdata(img)[0]
			data = caixaPixels(data,(coordx,coordy,Cdimension))	
			fluxo, sigma = calcFluxo(data, etime[i], medianBackground[i], stdBackground[i], ganho)
			vetorFluxoCamera.append(fluxo)
			vetorSigmaBackground_Signal.append(sigma)			
			i+=1				
		f.close()
		os.chdir(cwd)	
	criaArqFluxoCamera(vetorFluxoCamera, vetorSigmaBackground_Signal)
	


def caixaPixels(imagem, tupla):
	#retira apenas uma caixa de pixels, dada as coordenadas (x,y) e seu tamanho			
	xcoord = tupla[0]
	ycoord = tupla[1]
	dimension = tupla[2]/2
	d = dimension
	imagem = imagem[xcoord-d:xcoord+d,ycoord-d:ycoord+d]
	return imagem


def calcFluxo(data, etime, medianBackground, stdBackground, ganho):
	Somapixels, sigmaBackground_sigmaSignal, variance = 0, 0, 0
	Somapixels = sum(sum(data - medianBackground))*ganho #soma dos valores dos pixels subt. do Background mediano
	for linha in data:
		for pixel in linha:
			fluxo_e = (pixel-medianBackground)*ganho			
			variance += np.abs(fluxo_e) + (stdBackground*ganho)**2
	fluxoImagem = Somapixels/etime #contagens totais pelo tempo de exposicao
		
	return fluxoImagem, sqrt(variance)




def FluxoRelativo(Fluxocamera,Fluxodetector, Stdcamera, Strespectro, nomeArq_CalibDetector):
	
	vetorEQ, vetorSigmaTotal = [], []
	Split_Str_espectro = Strespectro.split(',')
	Einicial = int(Split_Str_espectro[0])
	Efinal   = int(Split_Str_espectro[1])
	step     = int(Split_Str_espectro[2])
	n = (Efinal - Einicial)/step
	espectro = np.linspace(Einicial, Efinal, n+1)

	VetorCalibracaoDetector = LeArq_curvaCalibDetector(nomeArq_CalibDetector, n+1)

	for i in range(len(Fluxocamera)):
		e = 1.60217653e-19
		ErroPorcentDetector = CalcErroDetector(espectro[i])
		sigmaDetector = sqrt(ErroPorcentDetector*Fluxodetector[i]**2)		

		EQ = Fluxocamera[i]*e/(Fluxodetector[i]*VetorCalibracaoDetector[i])*100	
		varianceTotal = (Stdcamera[i]*e/(Fluxodetector[i]))**2 +sigmaDetector**2
		vetorEQ.append(EQ)
		vetorSigmaTotal.append(sqrt(varianceTotal))
		i+=1

	return vetorEQ, vetorSigmaTotal




def getVetorEtime(nImages):
	arquivoListaImagens = 'listaImagens'
	vetorEtime = []
	listaImagens = LeArquivoReturnLista(arquivoListaImagens)
	for i in range(len(listaImagens))[::nImages]:
		header = fits.getheader(listaImagens[i])
		vetorEtime.append(header['exposure'])
	return vetorEtime

		


def getDadosBackground():
	dadosBackground = [[],[]]
	with open('dadosBackground.dat') as arq:
		listaValues = arq.read().splitlines()
		for linha in listaValues[1:]:
			values = linha.split('\t\t')
			dadosBackground[0].append(float(values[0]))
			dadosBackground[1].append(float(values[1]))
		arq.close()
	return dadosBackground




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
	return ErroDetector




def criaArqFluxoCamera(VetorF, vetorSigma):
	nome = 'Fluxo camera.dat'
	try: 
		arq = open(nome, 'w')
	except:
		nome.remove()
		arq = open(nome, 'w')
	arq.write(' Fluxo (W/m²)			Sigma\n')
	for i in range(len(VetorF)):
		arq.write('%e \t\t\t %f\n' %(VetorF[i], vetorSigma[i]))
	arq.close()


