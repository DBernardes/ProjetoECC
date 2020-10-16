#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 10 de Agosto de 2016 
    Descricao: este modulo tem como input uma imagem gerada pela biblioteca geraArquivo.py. Sobre essa imagem, o script ira criar tres graficos de saida, onde e possivel observar a variacao de contagens ao longo eixos horizontal e vertical; associado a cada um, tem-se os valores da media, desvio padrao absoluto e a quantidade de pixels inclusos dentro desse intervalo entre media +/- desvio. Ainda sobre esses dois eixos, foi tomada o valor de mediana para intervalos de bins pre-estabelecidos, assim como o desvio padrao absoluto. Foi feita uma relacao entre este desvio, e o desvio total para cada imagem, de modo que é possivel determinar se o ruido pixel-a-pixel está dentro do esperado.
	Esta biblioteca possui as seguintes funcoes:

		geraDados: esta funcao faz a leitura da imagem, retornando a media das linhas e das colunas.

		caixaInfo: esta funcao recebe as principais informacoes de todos os graficos, retornando um texto editado de seus valores.

		plotGradiente: esta funcao plota o vetor das medias em funcao das linhas ou das colunas da imagem.

		plotImagem: esta funcao plota a imagem fornecida subtraida de sua media.

		gradiente: esta funcao recebe a imagem combinada e faz o gerenciamento de todas as outras funcoes para a apresentacao do grafico.
	
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
        
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


import numpy as np
import matplotlib.pyplot as plt

from binagem import binagem 
from linhaReferencia import linhaReferencia
from returnMax import returnMax
from algarismoSig import algarismoSig

def CalcMean_Lin_Col(image):
	#variaveis de controle	
	meanLinha = []
	meanColuna = []
	nColunas = len(image[0])
	nLinhas = len(image)

	i=0
	while i < nLinhas:
		meanL = np.mean(image[i])
		meanLinha.append(meanL) # Gradiente de contagens ao longo do eixo vertical	
		i+=1		
	
	j=0
	while j < nColunas:
		k=0
		vetorColuna = []
		while k < nLinhas:
			vetorColuna.append(image[k][j])		
			k+=1		
		meanC = np.mean(vetorColuna)	
		meanColuna.append(meanC) #Gradiente de contagens ao longo do eixo horizontal
		j+=1

	return meanLinha, meanColuna



#Caixa de texto com media, mediana e seus desvios
def caixaInfo(vetorx,vetory, meanBinX, stdBinX, meanBinY,stdBinY):	

	stdx = np.std(vetorx)
	num = algarismoSig(stdx)
	stdx = round(stdx, num)

	num = algarismoSig(stdBinX)
	meanBinX = round(meanBinX,num)
	stdBinX  = round(stdBinX,num)

	stdRelativeX = stdx/stdBinX

	stdy = np.std(vetory)	
	num  = algarismoSig(stdy)
	stdy = round(stdy, num)

	num = algarismoSig(stdBinY)
	meanBinY = round(meanBinY,num)
	stdBinY  = round(stdBinY,num)
	
	stdRelativeY = stdy/stdBinY
	

	meanBinX = str(meanBinX)
	stdBinX  = str(stdBinX)
	meanBinY = str(meanBinY)
	stdBinY  = str(stdBinY)


	fonte = 24	
	sinal=None
	textstr0 = r'$\mathtt{Gradiente:}$'
	textstr1 = r'$\mathtt{Eixo \quad Y \; ---------}$'
	textstr2 = r'$\mathtt{\barF_{bin}= \; %s_-^+ \; %s \;\; adu} }$' %(meanBinX, stdBinX)	
	textstr3 = r'$\mathtt{\sigma_x = \; %.1f \;\; \bar\sigma_{bin}}$' %(stdRelativeX)	
	if 0.9 < stdRelativeX < 1.1:
		sinal = [r'$\mathtt{\approx}$', '']		
	if stdRelativeX > 1.1:
		sinal = [r'$\mathtt{\gg}$', r'$\mathtt{(> \; 10}$' +' %' + r'$\mathtt{)}$']
	if stdRelativeX < 0.9:
		sinal = [r'$\mathtt{\ll}$', r'$\mathtt{(< \; 10}$' +' %' + r'$\mathtt{)}$']

	textstr4 = r'$\mathtt{\sigma_x \;}$' + sinal[0] + r'$\mathtt{\; \sigma_{bin} \; }$'+sinal[1]


	textstr5 = r'$\mathtt{Eixo \quad X \; ---------}$'
	textstr6 = r'$\mathtt{\barF_{bin}= \; %s_-^+ \; %s \;\; adu} }$' %(meanBinY, stdBinY)	
	textstr7 = r'$\mathtt{\sigma_y = \; %.1f \;\; \bar\sigma_{bin}}$' %(stdRelativeY)	
	if 0.9 < stdRelativeY < 1.1:
		sinal = [r'$\mathtt{\approx}$', '']		
	if stdRelativeY > 1.1:
		sinal = [r'$\mathtt{\gg}$', r'$\mathtt{(> \; 10}$' +' %' + r'$\mathtt{)}$']
	if stdRelativeY < 0.9:
		sinal = [r'$\mathtt{\ll}$', r'$\mathtt{(< \; 10}$' +' %' + r'$\mathtt{)}$']

	textstr8 = r'$\mathtt{\sigma_y \;}$' + sinal[0] + r'$\mathtt{\; \sigma_{bin} \; }$'+sinal[1]

	textstr = [textstr0,textstr1,textstr2,textstr3,textstr4,textstr5,textstr6,textstr7,textstr8]
	return textstr


#plota grafico dos pixels
def plotGradiente(posx, posy, Vetormean, eixo = 'x'):
	font=20
	nDados = len(Vetormean)
	mean = np.mean(Vetormean)
	std = np.std(Vetormean)
	ax= plt.subplot2grid((4,3),(posx,posy),colspan=1)
	x = np.linspace(0, nDados, nDados)

	num = algarismoSig(std)
	mean = str(round(mean,num))
	std = str(round(std,num))


	if eixo == 'x':
		textstr =r'$\mathtt{\barF_y = %s_-^+ \; %s \quad adu}$' %(mean, std)	
		strX = r'$\mathtt{x (pixel)}$'
		strY = r'$\mathtt{M \acutee dia \; das \; contagens \; em \; Y}$'
	else:
		textstr =r'$\mathtt{\barF_x = %s_-^+ \; %s \quad adu }$' %(mean, std)		
		strX =  r'$\mathtt{y (pixel)}$'
		strY =  r'$\mathtt{M \acutee dia \; das \; contagens \; em \; X}$'
	plt.plot(x,Vetormean, color='gray',alpha=0.8)
	plt.xlim(0,nDados)
	plt.xlabel(strX,size=font)
	plt.ylabel(strY,size=font)	
	plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
	plt.text(0.05,0.90, textstr, va='center', ha='left', size=20,  transform=ax.transAxes)
	linhaReferencia(Vetormean)
	meanBin, meanStdBin = binagem(x,Vetormean)
	

	return meanBin,meanStdBin



def plotImagem(image):
	#imagem bidimensional dos pixels
	font=20
	mean = np.mean(image)
	img = image - mean
	mean = np.mean(img)
	std = np.std(img)		
	ax1= plt.subplot2grid((4,3),(0,0))
	plt.imshow(img,cmap='Blues',vmin=mean-std,vmax=mean+std,origin='lower', aspect='auto')
	plt.xlabel(r'$\mathtt{x (pixel)}$',size=font)
	plt.ylabel(r'$\mathtt{y (pixel)}$',size=font)
	plt.title (r'$\mathtt{Res \acute\iota duos:Rij=Fij-mediana}$',size=font) 	




#-------------------------------------------------------------------------------------------------
def gradiente(image):	
	print('Calculando gradiente da imagem ...')

	plotImagem(image)

	#gera vetor com media de linhas e colunas
	MeanLinha, MeanColuna = CalcMean_Lin_Col(image)	
	#plota graficos em cada direcao
	meanBinX,StdBinX = plotGradiente(0,1,MeanLinha,eixo='y')	
	meanBinY,StdBinY = plotGradiente(1,0,MeanColuna)

	textstr = caixaInfo(MeanLinha,MeanColuna, meanBinX,StdBinX, meanBinY,StdBinY)		

	return textstr
	
	


