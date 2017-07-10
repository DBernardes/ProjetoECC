#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 29 de Agosto de 2016  
    Descricao: este modulo visa reunir as bibliotecas responsaveis para a caracterizacao do ruido de leitura: variacaoTemporal, geraArquivo, gradiente, biashistogram, CCDinfo, caixaTexto, logfile, makeList_imagesInput. O codigo ira criar um arquivo contendo a lista de nomes das imagens; dessa lista ira retirar uma amostra de 10 imagens e retorna-la para as funcoes gradiente e histograma. A funcao gradiente ira expressar em um grafico em cores a variacao das contagens dos pixels ao longo desta imagem mediana, junto de dois outros graficos da variacao da media das constagens ao longo de suas linhas e colunas; a funcao histograma ira calcular uma distribuicao de frequencia das contagens para um intervalo da media dos pixels +/- 7sigmas. A funcao variacaoTemporal ira receber a lista de imagens completa, retornando um grafico com a mediana das contagens de cada imagem em funcao do tempo do experimento. Sobre esses dados e realizada uma FFT; e gerada uma segunda lista de dados normais em relacao a media e desvio padrao dos dados originais, de modo que a FFT desta serie e plotada junto a primeira, permitindo comparar os picos com intensidade acima de media+3sigmas.
		
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import datetime
import getpass
import socket
import numpy as np

import ConstructTextBox
from RNvariacaoTemporal import variacaoTemporal
from RNgradiente import gradiente
from RNhistograma import histograma
from CreateLogFile import logfile
from criaArq_resultadoCaract import arquivoCaract

from ccdproc import Combiner, CCDData
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l","--logfile", action="store_true", dest="logfile", help="Log file",default=False)

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./calcbias.py -h ";sys.exit(1);

class ReadNoiseCharact:

	def iniciaObjeto(self):
		self.cwd = os.getcwd()	
		RNobject.criaArq_listaImgInput()
		RNobject.readArq_returnlistImages()		
		self.header = fits.getheader(self.listaImagensBias[0]) #aquisicao do header
		nowInitial = datetime.datetime.now()
		self.minute, self.second = nowInitial.minute, nowInitial.second 	
		self.BackDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)



	def printListImgs(self):
		print self.listaImagensBias



	def criaArq_listaImgInput(self, nImages=1):
		s,i='',0	
		listaImagens = os.listdir(self.cwd)
		listaImagensFiltrada = []
		for img in listaImagens:
			if '.fits' in img:
				listaImagensFiltrada.append(img)
		listaImagensFiltrada.sort()
	
		for img in listaImagensFiltrada:
			if i%nImages == nImages-1:  
				s += str(img)+'\n'
			else: 
				s += str(img)+','
			i+=1		
		try:
			logf = open('listaImagens', 'w') 
		except:
			name.remove()
			logf = open('listaImagens', 'w')
		logf.write(s)
		logf.close()




	def readArq_returnlistImages(self):
		with open('listaImagens') as arq:
   			self.listaImagensBias = arq.read().splitlines()
			arq.close()



	def combinaImagensBias(self, numeroImagens=10):
		newlist, dados, i = [], [], 0
		step = len(self.listaImagensBias)/numeroImagens
		while i < numeroImagens:
			newlist.append(self.listaImagensBias[i*step])		
			i+=1
		for img in newlist:
			dados.append(fits.getdata(img, 0)[0])		
		#gera um outro vetor na classe CCDData
		x = []
		for img in dados:
			x.append(CCDData(img, unit = 'adu'))
			i+=1
		
		combinedImage = Combiner(x)
		combinedImageMedian = combinedImage.average_combine() #average_median
		self.NPcombinedImage = np.asarray(combinedImageMedian)	




	def CaractGradiente(self):
		self.StrGradiente  = gradiente(self.NPcombinedImage)
		
	
	def CaractHistograma(self):
		self.StrHistograma = histograma(self.NPcombinedImage)
		
		
	def CaractVariacaoTemporal(self):
		self.ruidoCalculado = variacaoTemporal(self.listaImagensBias)

	def InfoCaixaTexto(self):
		Strtemperatura = [r'$\mathtt{Temperatura: %i^oC}$' %(self.header['temp'])]
		textstr = Strtemperatura + self.StrGradiente + self.StrHistograma
		ConstructTextBox.textBox(textstr, 4, 3, 0, 2, font=24, space=0.05, rspan=2)

	def salvaArquivosResultados(self):
		os.chdir(self.BackDir)
		plt.savefig('Relatório Bias', format='pdf')
		os.chdir(self.cwd)

		dic = {'minute':self.minute, 'second':self.second,'ruidoNominal':self.ruidoCalculado, 'header':self.header}
		if options.logfile :
			print 'Criando arquivo log', '\n'
			logfile(dic, self.NPcombinedImage)	

		os.chdir(self.BackDir)
		arqCaract = arquivoCaract()
		arqCaract.criaArq(arqCaract)


RNobject = ReadNoiseCharact()
RNobject.iniciaObjeto()
plt.figure(figsize=(22,28))
RNobject.combinaImagensBias()
RNobject.CaractGradiente()
RNobject.CaractHistograma()
RNobject.CaractVariacaoTemporal()
RNobject.InfoCaixaTexto()
RNobject.salvaArquivosResultados()

