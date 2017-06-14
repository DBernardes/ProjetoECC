#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    Descricao: este codigo reune todas as bibliotecas responsaveis para a caracterizacao do ganho do CCD, sao elas: plotGraph, logfile, makeList_imagesInput e Gain_processesImages. O codigo ira criar duas listas de imagens: flat e bias, realizando o calculo da instensidade do sinal em funcao da variancia. Esses dados serao usado na plotagem de um grafico linear e, por meio do coeficiente angular de um ajuste linear calculado,  obtem-se o ganho; um segundo grafico e plotado onde aparece o resultado da subtracao dos dados obtidos pelos valores de um ajuste linear calculado.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./ganhoCompleto.py -f'Flat','nImages' -b'Bias' 

	Esta lista fornecida ao programa deve conter as imagens de bias e as imagens flat associdas em conjunto na forma
biasA,biasB,flatA,flatB.
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """



import os, sys
import matplotlib.pyplot as plt
import datetime


from optparse import OptionParser
from plotGraph import Graph_sinal_variance, Graph_residuos
from logfile import logfile
from makeList_imagesInput import criaArq_listaImgInput, LeArquivoReturnLista
from Gain_processesImages import calcXY_YerrorBar_XerrorBar, parametrosCaixaPixels
from criaArq_resultadoCaract import arquivoCaract

from astropy.io import fits

nowInitial = datetime.datetime.now()
minute = nowInitial.minute
second = nowInitial.second

parser = OptionParser()
parser.add_option("-l", "--logfile", action='store_true', dest="logfile", help="Arquivo Log",default="")
parser.add_option("-f", "--Flat", dest="flat", help="nome e num imagens flat",type='string',default="")
parser.add_option("-b", "--Bias", dest="bias", help="nome imagens bias",type='string',default="")
parser.add_option("-c", "--caixaPixels", dest="caixaP", help="parametros caixa pixel",type='string',default="")
try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./ganhoCompleto.py -h ";sys.exit(1);


if options.flat:
	parametros = options.flat.split(',')
	nameFlat      =	parametros[0]
	numeroImagens =	int(parametros[1])
if options.bias:
	nameBias = options.bias

criaArq_listaImgInput(numeroImagens, nameFlat)
criaArq_listaImgInput(1, nameBias)
listaBias = LeArquivoReturnLista(nameBias+'list')
listaFlat = LeArquivoReturnLista(nameFlat+'list')

#----------------------------------------------------------------------------------------------------------------------
parametersBox = parametrosCaixaPixels(options.caixaP, listaFlat[0])		
X,Y,SigmaTotal, XsigmaBar = calcXY_YerrorBar_XerrorBar(listaFlat, listaBias, numeroImagens, parametersBox)

plt.figure(figsize=(17,8))
ganho = Graph_sinal_variance(X,Y,SigmaTotal, XsigmaBar)
Graph_residuos(X,Y, SigmaTotal)


#gera arquivo log
if options.logfile:
	nImagesFlat = len(listaFlat)
	nImagesBias = len(listaBias)
	
	dic = {'minute':minute, 'second':second, 'nImagesFlat':nImagesFlat,'nImagesBias':nImagesBias, 'ganho':ganho, 'box':parametersBox}
	logfile(dic, listaFlat, listaBias)			


arqCaract = arquivoCaract()
arqCaract.criaArq(arqCaract)

