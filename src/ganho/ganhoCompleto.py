#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    Descricao: este modulo reune as bibliotecas reduction, readImages, flatCorrection, plotGraph e logfile, retornando um grafico com a intensidade de luz para cada imagem em funcao da variancia dos pixels. Atraves desse grafico e feito um ajuste linear e, pela sua derivada, calculado o ganho do CCD.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./ganhoCompleto.py --list=list

	Esta lista fornecida ao programa deve conter as imagens de bias e as imagens flat associdas em conjunto na forma
biasA,biasB,flatA,flatB.
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """



import os, sys
import numpy as np
import matplotlib.pyplot as plt
import datetime

from math import sqrt
from optparse import OptionParser
from readImages import readImages
from plotGraph import plotGraph
from logfile import logfile
from flatCorrection import flatCorrection

from astropy.io import fits

nowInitial = datetime.datetime.now()
minute = nowInitial.minute
second = nowInitial.second

parser = OptionParser()
parser.add_option("-i", "--list", dest="list", help="series bias e flat",type='string',default="")
parser.add_option("-l", "--logfile", dest="logfile", help="Arquivo Log",type='string',default="")

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./calcbias.py -h ";sys.exit(1);

#le cada lista de flat
if options.list:
	listaBiasA,listaBiasB,listaFlatA,listaFlatB=[],[],[],[]	
	with open(options.list) as f:
		lista = f.read().splitlines()		
		for linha in lista:
			Imgconjunto = linha.split(',')
			listaBiasA.append(Imgconjunto[0])
			listaBiasB.append(Imgconjunto[1])
			listaFlatA.append(Imgconjunto[2])
			listaFlatB.append(Imgconjunto[3])
	biasA, header = readImages(listaBiasA)
	biasB, header = readImages(listaBiasB)
	flatA, header = readImages(listaFlatA)
	flatB, header = readImages(listaFlatB)	



def calcXY(flatA, flatB, biasA, biasB):
	i=0
	g=0
	Y = []	
	X = []	
	std = []
	while i < len(flatA):
		sigmaBias = np.std(biasA[i] - biasB[i])
		sigmaFlat = np.std(flatA[i] - flatB[i])
		dadoy = (np.median(flatA[i])+np.median(flatB[i]) - np.median(biasA[i]) - np.median(biasB[i]))/(sqrt(2)*sigmaBias)
		dadox = sigmaFlat**2/(sigmaBias*sqrt(2))			
		Y.append(dadoy)
		X.append(dadox)		
		std.append(np.std(flatA[i])+np.std(flatB[i])+np.std(biasA[i])+np.std(biasB[i]))
		i+=1	
	return X,Y,std


box=0
def returnCaixaPixels(vetor, box=100):
	lenVetor = len(vetor)
	i, b = 0, box/2
	while i<lenVetor:
		vetor[i] = vetor[i][1000-b:1000+b,1000-b:1000+b]
		i+=1
	return vetor
	
#----------------------------------------------------------------------------------------------------------------------
flatA = returnCaixaPixels(flatA)
flatB = returnCaixaPixels(flatB)
biasA = returnCaixaPixels(biasA)
biasB = returnCaixaPixels(biasB)

X,Y,std = calcXY(flatA, flatB, biasA, biasB)
ganho = plotGraph(X,Y, std)
plt.savefig('ganho', format='jpg')
plt.close()

#gera arquivo log
if options.logfile:
	lenDados = len(flatA)*4
	dic = {'minute':minute, 'second':second, 'lenDados':lenDados, 'ganho':ganho, 'box':box, 'header':header}
	logfile(options.logfile, dic)	


